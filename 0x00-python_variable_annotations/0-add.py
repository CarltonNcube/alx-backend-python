#!/usr/bin/env python3
"""
This module defines a function that adds two floats.
"""

def add(a: float, b: float) -> float:
    """
    Add two floats.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
