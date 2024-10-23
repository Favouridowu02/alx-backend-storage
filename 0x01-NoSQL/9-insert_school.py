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
    new_obj = mongo_collection.insert_one(kwargs)
    return new_obj.inserted_id
