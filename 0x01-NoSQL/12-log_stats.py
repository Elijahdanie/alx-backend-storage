#!/usr/bin/env python3
"""
This module demonstrates collections and
documents in mongo db
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Fetches and format status, HTTP Request
    and logs information in the logs collection
    """
    client = MongoClient()
    collection = client.logs.nginx
    http_request = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    total_logs = collection.count()
    print('{} logs'.format(total_logs))
    print('Methods:')
    for req in http_request:
        count = collection.count()({"method": req})
        print('\tmethod {}: {}'.format(req, count))

    stats = collection.count(
        {"method": "GET", "path": "/status"}
        )
    print('{} status check'.format(stats))
