#!/usr/bin/env python3

"""
This module demonstrates querying
mongodb collection with a constraint
"""


def schools_by_topic(mongo_collection, topic):
    """
    This functions returns a list of
    all documents in the collection mongo_collection
    with the topic specified in the arguments
    """
    result = mongo_collection.find({"topics":  {"$in": [topic]}})
    return result
