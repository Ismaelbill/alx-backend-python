#!/usr/bin/env python3
""" More involved type annotations """
import typing as t


T = t.TypeVar('T')


def safely_get_value(dct: t.Mapping, key: t.Any, default: t.Union[
                            T, None] = None) -> t.Union[t.Any, T]:
    """ function checks if a key in a dict and returns if it is, else none"""
    if key in dct:
        return dct[key]
    else:
        return default
