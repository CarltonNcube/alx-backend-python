#!/usr/bin/env python3
"""
Defines a coroutine that collects 10 random numbers using async comprehensions.
"""

import asyncio
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[int]:
    """
    Asynchronously collects 10 random numbers using async comprehensions.

    Returns:
        List[int]: A list containing 10 random numbers.
    """
    random_numbers = [random_number async for random_number in async_generator()]
    
    return random_numbers
