#!/usr/bin/env python3
"""
This module defines a function that safely retrieves the first element of a list.
"""

from typing import Any, List, Union

def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element of a list.

    Args:
        lst (List[Any]): The input list.

    Returns:
        Union[Any, None]: The first element of the list, or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
