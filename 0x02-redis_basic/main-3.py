#!/usr/bin/python3
"""
    this is main-3.py
"""
import redis


replay = __import__('exercise').replay
Cache = __import__('exercise').Cache

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
