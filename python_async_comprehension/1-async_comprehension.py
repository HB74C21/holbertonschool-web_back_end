#!/usr/bin/env python3
"""
Coroutine that asynchronously collects random numbers using async comprehension
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator
    """
    return [number async for number in async_generator()]
