#!/usr/bin/env python3
"""
Defines a function to create an asyncio.Task from wait_random function.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from wait_random function.
    """
    return asyncio.Task(wait_random(max_delay))
