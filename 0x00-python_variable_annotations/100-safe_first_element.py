#!/usr/bin/env python3
"""  Duck typing - first element of a sequence """
import typing as t


def safe_first_element(lst: t.Sequence[t.Any]) -> t.Union[t.Any, None]:
    """ function returns either index 0 of lst, else None"""
    if lst:
        return lst[0]
    else:
        return None
