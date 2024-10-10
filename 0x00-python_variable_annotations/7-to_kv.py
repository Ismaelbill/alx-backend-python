#!/usr/bin/env python3
import typing as t
""" Complex types - string and int/float to tuple """


def to_kv(k: str, v: t.Union[int, float]) -> t.Tuple[str, float]:
    """ returns a tuple with k and v """
    return (k, v * v)
