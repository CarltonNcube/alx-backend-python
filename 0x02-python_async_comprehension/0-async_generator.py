#!/usr/bin/env python3
"""
Defines a coroutine that generates random numbers asynchronously.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """
    Asynchronously generates random numbers between 0 and 10.

    Yields:
        int: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
