#!/usr/bin/env python3
"""
A Python function that updates the topics
of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document based on the name.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topic": topics}})
