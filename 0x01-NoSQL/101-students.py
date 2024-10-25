#!/usr/bin/env python3
"""
    This Module contains a Python function that returns all students
    sorted by average score
"""


def top_students(mongo_collection):
    """
        This Function returns aall students sorted by average score

        Arguments:
            mongo_collection: This is a pymongo collection object

        Return: all students sorted by average score
    """
    list_students = mongo_collection.aggregate(
            [
                {
                    "$project": {
                        "_id": 1,
                        "name": 1,
                        "averageScore": {"$avg": "$topics.score"}
                        }
                },
                {
                    '$sort': {"averageScore": -1}
                }
            ])
    return list_students
