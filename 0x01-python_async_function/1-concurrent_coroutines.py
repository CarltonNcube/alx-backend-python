#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import time
from basic_async_syntax import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures and returns the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each call to wait_n.

    Returns:
        float: Average time taken for each call to wait_n.
    """
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
