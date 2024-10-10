#!/usr/bin/env python3
import typing as t
""" iterable  object """


def element_length(lst: t.Iterable[t.Sequence]) -> t.List[
                        t.Tuple[t.Sequence, int]]:
    """ returns a list """
    return [(i, len(i)) for i in lst]
