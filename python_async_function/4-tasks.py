#!/usr/bin/env python3
"""
Asynchronously waits for random delays and
returns a sorted list of the results
"""

from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for random delays
    and returns a sorted list of the results
    """
    list_random = []
    for _ in range(n):
        list_random.append(await task_wait_random(max_delay))
    return sorted(list_random)
