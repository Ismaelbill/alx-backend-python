#!/usr/bin/env python3
"""  Complex types - mixed list """
import typing as t


def sum_mixed_list(mix_lst: t.List[t.Union[int, float]]) -> float:
    """ list of integers and floats,
    returns their sum as a float"""
    j: float = 0.0
    for i in mix_lst:
        j += i
    return j
