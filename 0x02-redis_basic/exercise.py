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
        return self._redis.get(key), lambda x: x.decode('utf-8')

    def get_int(self, key: str) -> int:
        return self._redis.get(key, int)
