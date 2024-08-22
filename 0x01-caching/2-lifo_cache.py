#!/usr/bin/env python3
"""LIFO caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """__init__ function"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded = self.order.pop()
                    del self.cache_data[discarded]
                    print(f"DISCARD: {discarded}")

            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """get function"""
        return self.cache_data.get(key) if key is not None else None
