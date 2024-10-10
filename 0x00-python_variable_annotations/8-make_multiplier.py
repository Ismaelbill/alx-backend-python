#!/usr/bin/env python3
import typing as t
""" Complex types - functions """


def make_multiplier(multiplier: float) -> t.Callable[[float], float]:
    """ creating another func that will multiply by any float given,
    returns `multiply` func"""
    def multiply(n: float) -> float:
        """ it multiplies the numbers that were given and return the result"""
        return n * multiplier
    return multiply
