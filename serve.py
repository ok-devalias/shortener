import webapp2
import datetime
import string
import random
from google.appengine.ext import ndb
from google.appengine.api import memcache
from models import LinkMap

class Serve(webapp2.RequestHandler):
  """ Redirects shortened to true URL """
  def get(self):
    if len(self.request.path.split('/')) > 1:
      key = self.request.path.split('/')[2]
      url = memcache.get(key)
      if url is None:
        dbkey = ndb.Key(LinkMap, key)
        linkmap = dbkey.get()
        url = linkmap.url
      return self.redirect(str(url))

app = webapp2.WSGIApplication([('/r/.*', Serve)])
