#!/usr/bin/env python3
"""
Module that imports function
the coroutine will execute it 4 times in parallel
using asyncio.gather
measure runtime and return it
"""


import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Return measured runtime"""
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.time()

    return end - start
