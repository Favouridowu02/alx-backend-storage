#!/usr/bin/env python3
"""
    This Module contains a function that lists all documents on a
    collection
"""
import pymongo


def list_all(mongo_collection):
    """
        This Function lists all documents in a collection

        Arguments:
            mongo_collection: This is a pymongo collection object
    """
    mongo_list = []
    for doc in mongo_collection.find():
        mongo_list.append(doc)
    return mongo_list
