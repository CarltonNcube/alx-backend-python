#!/usr/bin/env python3
"""Importing the asyncio module for asynchronous programming"""

import asyncio
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: List of all the delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
