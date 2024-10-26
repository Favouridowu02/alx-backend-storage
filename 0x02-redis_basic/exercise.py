#!/usr/bin/env python3
"""
    This Module contains a class Cache.
"""
import redis
from uuid import uuid4


class Cache:
    """
        This Class is a Cache class

        Methods:
            store: this method is used to store data
    """
    def __init__(self):
        """
            This is the initialization of the class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
            This method takes an argument and returns a string

            Arguments:
                data: The data to be stored

            Return: returns the random key used for storing
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
