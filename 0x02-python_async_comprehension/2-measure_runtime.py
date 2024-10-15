#!/usr/bin/env python3
""" calculating time it takes to run 4 coroutines async """

import time as tm
import asyncio as asy
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measuring the total runtime and return it """
    start: float = tm.time()
    await asy.gather(async_comprehension(), async_comprehension(),
                     async_comprehension(), async_comprehension())
    end: float = tm.time()
    return (end - start)
