#!/usr/bin/env python3
"""
A python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    school_list = mongo_collection.find({"topics": topic})

    return school_list
