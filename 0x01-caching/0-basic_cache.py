#!/usr/bin/env python3
""" First task file
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    """

    def __init__(self):
        """
        Initialize the class with the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Method to store a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value of given key or none.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
