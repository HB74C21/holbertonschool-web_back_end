#!/usr/bin/env python3
"""
Module containing a Server class to paginate a database of popular baby names
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.
        """
        assert type(page, int) and page > 0
        assert type(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)
        start_index, end_index = index_range(page, page_size, total_rows)

        if start_index >= total_rows:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve a hypermedia representation of the dataset page.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        dataset_page = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
