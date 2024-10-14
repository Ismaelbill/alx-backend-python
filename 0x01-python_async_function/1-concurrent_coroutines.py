#!/usr/bin/python3
"""executing multiple coroutines at the same time with async"""

import asyncio
import typing as t

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> t.List[float]:
    """wait_n - return the list of all the delays (float values)"""
    arr: t.List[float] = []
    var: float
    while n:
        ret = await wait_random(max_delay)
        arr.append(ret)
        n -= 1
    for i in range(len(arr)):
        for i in range(len(arr)-1):
            if (arr[i] > arr[i + 1]):
                var = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = var
    return arr
