#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """__init__ function"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded = self.order.pop(0)
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")

            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)

    def get(self, key):
        """get function"""
        return self.cache_data.get(key) if key is not None else None
