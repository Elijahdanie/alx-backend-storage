#!/usr/bin/env python3
"""
This module demonstrates collections and
documents in mongo db
"""


def update_topics(mongo_collection, name, topics):
    """
    This functions inserts a document in
    mongo_collection and returns the documentid
    """
    update = {'$set': {'topics': topics}}
    return mongo_collection.update_many({'name': name}, update)
