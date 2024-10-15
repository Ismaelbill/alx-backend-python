#!/usr/bin/env python3
""" Async Comprehensions """

import typing as t
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> t.List[float]:
    """ collecting 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers. """
    arr: t.List[float] = [a async for a in async_generator()]
    return arr
