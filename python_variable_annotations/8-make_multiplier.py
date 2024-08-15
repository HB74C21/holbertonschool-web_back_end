#!/usr/bin/env python3
"""
Defines a function to create a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a number by the given multiplier.
    """

    def multiplier_function(value: float) -> float:
        """
        Returns the result of multiplying x by the given multiplier.
        """
        return value * multiplier

    return multiplier_function
