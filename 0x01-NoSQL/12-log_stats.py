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
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    http_request = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    total_logs = db.nginx.count_documents({})
    print('{} logs'.format(total_logs))
    print('Methods:')
    cnginx = db.nginx
    for req in http_request:
        count = cnginx.count_documents({"method": req})
        print('\tmethod {}: {}'.format(req, count))

    stats = db.nginx.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print('{} status check'.format(stats))
