#!/usr/bin/env python3
"""Task"""


import typing as t
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> t.List[float]:
    """task_wait_n - return the list of all the delays (float values)"""
    arr: t.List[t.Any] = [task_wait_random(max_delay) for _ in range(n)]
    res = await asyncio.gather(*arr)
    return res
