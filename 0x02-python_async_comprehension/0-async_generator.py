#!/usr/bin/env python3
""" Async Generator """

import asyncio
import random
import typing as t


async def async_generator() -> t.Generator[float, None, None]:
    """ coroutine (async_generator) takes no argument
    loops 10 times, waits 1 second, then yield a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
