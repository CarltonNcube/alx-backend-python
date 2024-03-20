#!/usr/bin/env python3
"""Measures the runtime of executing async_comprehension."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension 4 times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
