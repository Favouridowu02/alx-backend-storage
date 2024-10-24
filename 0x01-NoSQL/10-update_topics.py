#!/usr/bin/env python3
"""
    This Module contains a function that changes all topics of a school
    document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
        This Module contains a Python function that changes all topics
        of a school document based on the name

        Arguments:
            mongo_collection: a pymongo collection object
            name: The school name to update
            topics: a List of Topics approached in the school
    """
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
    )
