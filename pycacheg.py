from collections import OrderedDict

class cache_LRU:
    """
    LRU in-memory cache implementation.
    Uses OrderedDict for LRU and key->value.
    """

    def __init__(self, size=10):
        self.size = size
        self.cached = OrderedDict()

    def addKey(self, key, value):
        if key in self.cached:
            return False
        else:
            self.setKey(key, value)
            return True

    def setKey(self, key, value):
        if key in self.cached:
            self.removeKey(key)
        self.checkEvict()
        self.cached[key] = value

    def getByKey(self, key):
        if key in self.cached:
            return self.cached[key]

    def removeKey(self, key):
        del self.cached[key]

    def checkEvict(self):
        """ popitem defaults to LIFO, so override for FIFO behavior. """
        if len(self.cached) >= self.size:
            self.cached.popitem(last=False)

#    def __init__(self, size=10):
#        self.size = size
#        self.cache = {}
#        self.used_keys = []
#    def addKey(self, key, value):
#        if key in self.cache:
#            return False
#        else:
#            self.setKey(key, value)
#            return True
#    def setKey(self, key, value):
#        if key in self.cache:
#            idx = self.used_keys.index(key)
#            self.used_keys[:] = self.used_keys[:idx] + self.used_keys[idx+1:]
#            self.used_keys.insert(0, key)
#        else:
#            if len(self.used_keys) == self.size:
#                self.removeKey(self, key)
#            self.cache[key] = value
#            self.used_keys.insert(0, key)
#    def getByKey(self, key):
#        if key in self.cache:
#            return self.cache[key]
#    def removeKey(self, key):
#        del self.cache[key]
#        del self.used_keys[self.used_keys.index(key)]
