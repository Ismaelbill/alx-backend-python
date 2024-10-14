#!/usr/bin/env python3
"""executing multiple coroutines at the same time with async"""

import asyncio
import typing as t

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> t.List[float]:
    """wait_n - return the list of all the delays (float values)
    updated code: """
    arr = [wait_random(max_delay) for _ in range(n)]
    iterator = asyncio.as_completed(arr)
    array = [await a for a in iterator]

    return array
