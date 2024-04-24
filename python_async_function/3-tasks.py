#!/usr/bin/env python3
"""
Defines a function to create an asyncio.Task from wait_random function.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    Create an asyncio.Task from wait_random function.
    """
    return asyncio.create_task(wait_random(max_delay))
