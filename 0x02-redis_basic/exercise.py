#!/usr/bin/env python3

"""
This module demonstrates working with the
python redis library.
"""

from typing import Callable
import redis
import uuid
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator that wraps around function calls and
    stores the metric for number of calls in th redis
    database using the function name as key
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper_func(self, *args, **kwargs):
        """
        the function wrapper f(n)
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper_func

def call_history(method: Callable) -> Callable:
    """decorator function to recode parameter & output history"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """function wrapper f(n)"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper

class Cache:
    def __init__(self):
        """
        Initializes the redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data):
        """
        Generates a uuid key and stores the data in redis
        returns the uuid key generated
        """
        key_param = str(uuid.uuid4())
        self._redis.set(key_param, data)
        return key_param

    def get(self, key: str, fn = None):
        """
        Retrieves the data from redis and calls the function
        if the data is not in redis
        """
        result = self._redis.get(key)
        if result:
            return result if fn is None else fn(result)
        else:
            return None

    def get_str(self, data: str)-> str:
        """
        thi returns a string conversion of the data
        """
        return str(data, 'utf-8')

    def get_int(self, data)-> int:
        """
        This returns a integer conversion of the byte json data
        """
        return int.from_bytes(data)
    