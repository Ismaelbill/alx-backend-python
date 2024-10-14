#!/usr/bin/python3
""" The basics of async """

import asyncio
import random as r


async def wait_random(max_delay: int =10) -> float:
    """ wait_random - waits for a random delay between 0
    and max_delay (included and float value)
    seconds and eventually returns it."""
    random_int: float = r.uniform(0, max_delay)
    await asyncio.sleep(random_int)
    return random_int
