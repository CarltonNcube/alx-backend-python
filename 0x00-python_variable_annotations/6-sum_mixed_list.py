#!/usr/bin/env python3
"""
This module defines a function that sums a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)
