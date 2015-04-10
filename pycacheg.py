

"""
LRU in-memory cache implementation.
Uses Hashmap for key->value, Linked List for eviction of
Least-Recently Used values.
Intended to be called from cache GAE module.
"""

class cache_LRU:

    def __init__(self, size=10):
        self.size = size
        self.cache = {}
        self.used_keys = []

    def addKey(self, key, value):
        if key in self.cache:
            return False
        else:
            setKey(self, key, value)
            return True

    def setKey(self, key, value):
        if key in self.cache:
            idx = self.used_keys.index(key)
            self.used_keys[:] = self.used_keys[:idx] + self.used_keys[idx+1:]
            self.used_keys.insert(0, key)
        else:
            if len(self.used_keys) = self.used_keys:
                self.removeKey(self, key)
            self.cache[key] = value
            self.used_keys.insert(key)

    def removeKey(self, key):
        del self.cache[key]
        del self.used_keys[self.used_keys.index(key)]
