#!/usr/bin/env python3

# import asyncio

# wait_random = __import__('0-basic_async_syntax').wait_random

# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))

arr = [1, 2, 3]
var = arr[1]
arr[1] = arr[2]
arr[2] = var
print(arr)
