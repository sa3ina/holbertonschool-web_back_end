#!/usr/bin/env python3
"""
Module that takes a float and returns function
that multiplies a float by multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies a function by multiplier"""

    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
