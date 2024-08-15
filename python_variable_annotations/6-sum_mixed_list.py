#!/usr/bin/env python3
"""
Defines a function to calculate the sum of a mixed list of integers and floats
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of numbers in a mixed list of integers and floats."""
    return sum(mxd_lst)
