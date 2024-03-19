#!/usr/bin/env python3
"""Creates a coroutine that generates random numbers asynchronously."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> Generator[float, None]:
    """
    Asynchronously generates random numbers between 0 and 10.

    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
