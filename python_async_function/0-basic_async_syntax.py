#!/usr/bin/env python3
"""
Defines a function to asynchronously wait for a random delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
