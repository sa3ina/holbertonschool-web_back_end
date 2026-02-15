#!/usr/bin/env python3
"""
Module that takes a list of integers and
floats and returns their sum as float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return list of floats and integers sum as float"""
    return sum(mxd_lst)
