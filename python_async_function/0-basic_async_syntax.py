#!/usr/bin/env python3
"""
Module for async coroutine that takes integer
and waits for a random delay and returns it
"""


import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Return random delay time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
