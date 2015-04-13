from pycacheg import cache_LRU
import random, string

def generate_key(length=8):
  allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
  return ''.join(random.choice(allowed) for i in range(length))

cache = cache_LRU()
print "Generating key value pairs."
kvpair = {generate_key(): generate_key(length=3) for n in range(0,10)}
overload = {generate_key(): generate_key(length=3) for n in range(0,2)}
print "Adding %s Keys..." % len(kvpair)
for k in kvpair.keys():
    print "Key: %s \nValue: %s" % (k,kvpair[k])
    cache.addKey(k, kvpair[k])
    print cache.cached

key = kvpair.keys()[0]
print "Getting by Key: " + key
keyval = cache.getByKey(key)
print "Value returned: " + keyval
print "Cache: "
print cache.cached
print "Removing Key..."
cache.removeKey(key)
print "Current Cache: "
print cache.cached
print "Adding key over maximum..."
for k in overload.keys():
    print "Key: %s \nValue: %s" % (k,overload[k])
    cache.addKey(k, overload[k])

print "Cache Size: %s" % len(cache.cached)
print cache.cached
