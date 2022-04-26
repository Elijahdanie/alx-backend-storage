#!/usr/bin/env python3
"""
This module demonstrates collections and
documents in mongo db
"""

def list_all(mongo_collection):
    """
    This functions returns a list of
    all documents in the collection mongo_collection
    """
    results = mongo_collection.find()
    return [] if results.count() == 0 else results
