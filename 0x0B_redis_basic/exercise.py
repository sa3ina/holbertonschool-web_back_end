#!/usr/bin/env python3
"""
Redis caching system with call history tracking.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Stores input and output history of calls in Redis."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(outputs_key, str(output))

        return output

    return wrapper


def replay(method):
    """Display the history of calls of a particular function."""

    r = redis.Redis()

    key = method.__qualname__
    inputs_key = f"{key}:inputs"
    outputs_key = f"{key}:outputs"

    inputs = r.lrange(inputs_key, 0, -1)
    outputs = r.lrange(outputs_key, 0, -1)

    print(f"{key} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        print(f"{key}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")


class Cache:
    """Redis caching system for storing data with call history support."""

    def __init__(self):
        """Initialize Redis instance and flush database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store a value in Redis and return its generated key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """Retrieve value from Redis with optional conversion function."""
        value = self._redis.get(key)

        if value is None:
            return None

        if fn:
            return fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string value from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer value from Redis."""
        return self.get(key, fn=int)
