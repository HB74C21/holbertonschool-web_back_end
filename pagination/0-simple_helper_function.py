#!/usr/bin/env python3
"""
function named index_range that takes two integer arguments page and page_size
"""

from typing import Tuple


def index_range(page, page_size)-> Tuple(int, int):
    """
    Calculate start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size + 1
    end_index = start_index + page_size

    return start_index, end_index
