#!/usr/bin/env python3
"""Measures the total execution time for wait_n(n, max_delay)"""
import asyncio
from basic_async_syntax import wait_n
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures and returns the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each call to wait_n.

    Returns:
        float: Average time taken for each call to wait_n.
    """
    async def measure():
        start_time = asyncio.get_event_loop().time()
        await wait_n(n, max_delay)
        end_time = asyncio.get_event_loop().time()
        total_time = end_time - start_time
        return total_time / n

    return asyncio.run(measure())
