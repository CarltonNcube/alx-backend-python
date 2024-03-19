#!/usr/bin/env python3
"""Measures the runtime of executing async_comprehension."""

import asyncio
from time import perf_counter

# Import async_comprehension coroutine from the previous task
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = perf_counter()
    return end_time - start_time
