#!/usr/bin/env python3
"""Execute multiple coroutines concurrently with asyncio"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    futures = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await future for future in asyncio.as_completed(futures)]
    return delays
