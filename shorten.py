import webapp2
import datetime
import string
import random
from google.appengine.ext import ndb
from google.appengine.api import memcache
from google.appengine.api import modules
from models import LinkMap

def generate_key(length=8):
  allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
  return ''.join(random.choice(allowed) for i in range(length))


class Shorten(webapp2.RequestHandler):
  """ Shortens passed URL """
  def get(self):
    if len(self.request.params) > 0:
      url = self.request.params['url']
      now = datetime.datetime.now()
      key = generate_key()
      added = False

      while not added:
        added = memcache.add(key=key, value=url)
        if not added:
          key = generate_key()

      linker = LinkMap(
        key = ndb.Key(LinkMap, key),
        url = url,
        created = now
      )
      linker.put()
      link = 'http://%s/r/%s' % (modules.get_hostname(module='serve'), key)
      d = {'link':link,'to':url,'created':now}
      linkjson = '{{ "link": "{link}", "to": "{to}", "created": "{created}" }}'

      self.response.write(linkjson.format(**d))
    else:
      self.response.write("Bad Request.")


app = webapp2.WSGIApplication([('/s/.*', Shorten)])
