#!/usr/bin/env python3


def schools_by_topic(mongo_collection, topic):
    """
    This functions returns a list of
    all documents in the collection mongo_collection
    with the topic specified in the arguments
    """
    results = mongo_collection.find({'$in': [topic]})
    return results
