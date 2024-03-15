#!/usr/bin/env python3
"""
This module defines a function that safely retrieves a value from a dictionary.
"""

from typing import Dict, TypeVar, Optional

# Define type variables
K = TypeVar('K')  # Type of keys in the dictionary
V = TypeVar('V')  # Type of values in the dictionary

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> V:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Dict[K, V]): The input dictionary.
        key (K): The key to retrieve the value for.
        default (Optional[V]): The default value to return if the key is not found.
        Defaults to None.

    Returns:
        V: The value associated with the key in the dictionary, or the 
        default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
