#!/usr/bin/env python3
"""Importing the asyncio module for asynchronous programming"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async oroutine that waits for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
