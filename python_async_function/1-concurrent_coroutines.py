#!/usr/bin/env python3
"""
Defines a function to asynchronously wait for multiple random delays.
"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for 'n' random delays with
    maximum delay 'max_delay'.
    """
    list_random = []
    for _ in range(n):
        list_random.append(await wait_random(max_delay))

    return sorted(list_random)
