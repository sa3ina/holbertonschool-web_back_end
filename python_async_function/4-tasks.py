#!/usr/bin/env python3
"""
Module that imports function
and alter it into a new function
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of delays"""
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
