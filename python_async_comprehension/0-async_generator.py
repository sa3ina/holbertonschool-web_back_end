#!/usr/bin/env python3
"""
Module providing coroutine that takes no arguments
will loop 10 times, each time async. wait 1 second
then yield a random number between 0 and 10
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Wait 1 second,return
    random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i
