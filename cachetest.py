from pycacheg import cache_LRU
import random, string

def generate_key(length=8):
  allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
  return ''.join(random.choice(allowed) for i in range(length))

cache = cache_LRU()
print "Adding Key..."
cache.addKey(generate_key(), generate_key(length=3))
key = cache.getKey(cache.used_keys[0])
print "Key: " + key
print "Removing Key..."
cache.removeKey(cache.cache.index(key))
print cache.cache
