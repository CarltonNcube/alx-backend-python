#!/usr/bin/env python3
"""Defines a function creating a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier."""
    def multiplier_function(x: float) -> float:
        """Multiply a float by the given multiplier."""
        return x * multiplier

    return multiplier_function
