#!/usr/bin/env python3
"""
Module that imports function
the coroutine collect 10 random numbers
and return it
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return collected 10 random numbers"""
    return [number async for number in async_generator()]
