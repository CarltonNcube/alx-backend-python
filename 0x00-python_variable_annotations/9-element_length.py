#!/usr/bin/env python3
"""
This module defines a function that calculates the length 
of each element in a list.
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list.

    Args:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple
        contains a sequence from the input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
