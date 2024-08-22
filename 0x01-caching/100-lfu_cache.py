#!/usr/bin/env python3
"""LFU caching"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """__init__ function"""
        super().__init__()
        self.frequency = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=lambda k: self.order.index(k))
                else:
                    lru_key = lfu_keys[0]
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                self.order.remove(lru_key)
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.frequency[key] += 1
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """get function"""
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
