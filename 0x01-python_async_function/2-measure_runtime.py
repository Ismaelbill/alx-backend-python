#!/usr/bin/env python3
""" measuring the runtime """

import time as t
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    start: float = t.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = t.time()
    return (end - start) / n
