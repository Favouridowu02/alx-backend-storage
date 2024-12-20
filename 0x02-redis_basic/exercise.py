#!/usr/bin/env python3
"""
    This Module contains a class Cache.
"""
import redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
        This is a decorator that is used to store how many times a
        method in the Cache has been called

        Arguments:
            method: the Callable function

        Return: returns a callable function
    """
    @wraps(method)
    def count(self, *arg) -> None:
        name = method.__qualname__
        self._redis.incr(name, 1)
        return method(self, *arg)
    return count


def call_history(method: Callable) -> Callable:
    """
        This is a decorator that is used to store the history of input
        and outputs

        Arguments:
            method: The Callable function

        Return: returns the output of method
    """
    @wraps(method)
    def history(self, *args) -> None:
        input_arg = f"{method.__qualname__}:inputs"
        output_arg = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_arg, str(args))
        output = method(self, *args)
        self._redis.rpush(output_arg, output)
        return output
    return history


def replay(method):
    """
        This is a function to display the history of calls of a
        particular function

        Arguments:
            method:  the function to be passed as a parameter
    """
    input_arg = f"{method.__qualname__}:inputs"
    output_arg = f"{method.__qualname__}:outputs"
    inputs = method.__self__._redis.lrange(input_arg, 0, -1)
    outputs = method.__self__._redis.lrange(output_arg, 0, -1)
    length = method.__self__._redis.llen(input_arg)

    name = method.__qualname__
    print(f'{name} was called {length} times:')
    for input_val, output_val in zip(inputs, outputs):
        input_val = input_val.decode('utf-8')
        output_val = output_val.decode('utf-8')
        print(f'{name}(*{input_val}) -> {output_val}')


class Cache:
    """
        This Class is a Cache class

        Methods:
            store: this method is used to store data
    """
    def __init__(self) -> None:
        """
            This is the initialization of the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            This method takes an argument and returns a string

            Arguments:
                data: The data to be stored

            Return: returns the random key used for storing
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """
            This method is used to get the value from the redis db
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
            This method is used to get a string representation of
            the
            data

            Argument:
                key: this is the key to be used to access the value

            Return: returns a string representation of the value
        """
        return self._redis.get(key), lambda x: x.decode('utf-8')

    def get_int(self, key: str) -> int:
        """
            This method is used to get an int representation of true
            data
            Argument:
                key: this is the key to be used to access the value

            Return: returns an int representation of the value
        """
        return self._redis.get(key, int)
