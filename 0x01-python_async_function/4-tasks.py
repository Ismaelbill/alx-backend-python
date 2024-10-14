#!/usr/bin/env python3
"""Task"""

import asyncio
import typing as t

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> t.List[float]:
    """task_wait_n - return the list of all the delays (float values)
    updated code"""
    arr = [task_wait_random(max_delay) for _ in range(n)]
    iterator = asyncio.as_completed(arr)
    array = [await a for a in iterator]

    return array
