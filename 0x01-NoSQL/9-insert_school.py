#!/usr/bin/env python3
"""
This module demonstrates collections and
documents in mongo db
"""

def insert_school(mongo_collection, **kwargs):
    """
    This functions inserts a document in
    mongo_collection and returns the documentid
    """
    return mongo_collection.insert(kwargs)
