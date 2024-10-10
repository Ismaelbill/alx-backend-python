#!/usr/bin/env python3
""" iterable  object """
import typing as t


def element_length(lst: t.Iterable[t.Sequence]) -> t.List[
                        t.Tuple[t.Sequence, int]]:
    """ returns a list """
    return [(i, len(i)) for i in lst]
