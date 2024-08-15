#!/usr/bin/env python3
"""
Defines a function to calculate the lengths of elements
in an iterable of sequences.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element
    of the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]
