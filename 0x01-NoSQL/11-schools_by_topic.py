#!/usr/bin/env python3
"""
    This Module contains a function that returns the list of school
    having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
        This function returns the list of school having a specific topic

        Arguments:
            mongo_collection: The is the mongo collection object
            topic: This is the topic to be used for checking
    """
    list_obj = mongo_collection.find({'topics': topic})
    return list_obj
