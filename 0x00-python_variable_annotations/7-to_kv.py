#!/usr/bin/env python3
"""
This module defines a function that creates a tuple with the square of an int
or float value.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the square of an int or float value.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string key and the square of
        the int or float value.
    """
    return (k, v * v)
