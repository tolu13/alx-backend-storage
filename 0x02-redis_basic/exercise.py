#!/usr/bin/env bash
"""
writing strings to redis

"""

import redis
import uuid
from typing import Union

class Cache:
    """
    cache class for storing and retrieving data using Redis

    """
    def __init__(self)-> None:
        """
        this initialize the cache class
        creates a Redis client instance and flushes the db

        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data in Redis with a randomly generated key

        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

