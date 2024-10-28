#!/usr/bin/env python3
"""
    This Module contains a function get_page that returns the html
    content of a particular url
"""
import requests
import redis
from functools import wraps
from typing import Callable

redis_storage = redis.Redis()


def data_cache(method: Callable) -> Callable:
    """Caches the output of fetched data"""
    @wraps(method)
    def invoker(args) -> str:
        """This is the invoker function"""
        redis_storage.incr(f"count:{args}")
        result = redis_storage.get(f"result:{args}")
        if result:
            return result.decode('utf-8')
        result = method(args)
        redis_storage.set(f"count:{args}", 0)
        redis_storage.setex(f"result:{args}", 10, result)
        return result
    return invoker


@data_cache
def get_page(url: str) -> str:
    """
        This function used the request module to obtain the html content
        of a particular URL and returns it.

        Arguments:
            url: the Uniform Resource Locator Link

        Return: returns the HTML
    """
    return requests.get(url).text
