#!/usr/bin/env python3
'''
Implementation of the wait_n coroutine
'''
import asyncio
import random

async def wait_n(n, max_delay):
    """
    Spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    return sorted(completed_tasks)

async def wait_random(max_delay: int) -> float:
    """Wait for a random delay and return the delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

