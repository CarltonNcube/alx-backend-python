#!/usr/bin/env python3
"""
This script defines a function to zoom in an array by replicating its elements.
"""

from typing import Tuple, Any

def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> Tuple[Any, ...]:
    """
    Zoom in an array by replicating its elements.

    Args:
        lst (Tuple[Any, ...]): The input array.
        factor (int): The zoom factor. Defaults to 2.

    Returns:
        Tuple[Any, ...]: The zoomed-in array.
    """
    zoomed_in: Tuple[Any, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
