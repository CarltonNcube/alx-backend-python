#!/usr/bin/env python3
"""Creates an asyncio.Task object for waiting for a random delay."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task object for waiting for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task object representing the asynchronous operation.
    """
    return asyncio.create_task(wait_random(max_delay))
