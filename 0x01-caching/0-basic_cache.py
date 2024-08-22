#!/usr/bin/env python3

"""Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        return self.cache_data.get(key) if key is not None else None
