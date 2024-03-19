#!/usr/bin/env python3
"""Defines a coroutine that generates random numbers asynchronously."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates random numbers between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
