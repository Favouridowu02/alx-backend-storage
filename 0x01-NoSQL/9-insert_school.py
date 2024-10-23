#!/usr/bin/env python3
"""
    This Module contains a function that inserts a new document in a
    collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
        A  function that inserts a new document in a collection based
        on kwargs
    """
    mongo_collection.insert_one(locals()["kwargs"])
    return mongo_collection.insert_id
