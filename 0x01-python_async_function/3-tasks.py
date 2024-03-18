#!/usr/bin/env python3
"""Creates an asyncio.Task object for waiting for a random delay."""

import asyncio
from typing import Task
from basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> Task:
    """
    Returns an asyncio.Task object for waiting for a random delay.
    
    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task object representing the asynchronous operation.
    """
    return asyncio.create_task(wait_random(max_delay))

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
