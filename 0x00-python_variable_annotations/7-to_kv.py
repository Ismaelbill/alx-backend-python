#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """
import typing as t


def to_kv(k: str, v: t.Union[int, float]) -> t.Tuple[str, float]:
    """ returns a tuple with k and v """
    return (k, v * v)
