#!/usr/bin/env bash
"""
writing strings to redis

"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    cache class for storing and retrieving data using Redis

    """
    def __init__(self) -> None:
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
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """
        retrieves data from redis
        returns: Union[str, bytes, int, float, None]

        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        rerieves data from Redis as a utf-8 string

        args:
            key (str): the key to retrieve
        returns:
            Optional[str]

        """
        return self.get(key, lambad d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        retrieves data from Redis as an integer

        """
        return self.get(key, lambda d: int(d))
