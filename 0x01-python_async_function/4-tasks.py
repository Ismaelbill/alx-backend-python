#!/usr/bin/env python3
"""Task"""


import typing as t

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> t.List[float]:
    """task_wait_n - return the list of all the delays (float values)"""
    arr: t.List[float] = []
    var: float
    while n:
        ret = await task_wait_random(max_delay)
        arr.append(ret)
        n -= 1
    for i in range(len(arr)):
        for i in range(len(arr)-1):
            if (arr[i] > arr[i + 1]):
                var = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = var
    return arr
