#!/usr/bin/env python3
"""
Module that takes string and int or float
and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple"""
    return (k, float(v ** 2))
