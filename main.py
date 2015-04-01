import webapp2
import datetime
import string
import random
from google.appengine.ext import ndb
from google.appengine.api import memcache

class LinkMap(ndb.Model):
  url = ndb.StringProperty(required=True)
  created = ndb.DateProperty()

def generate_key(length=8):
  allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
  return ''.join(random.choice(allowed) for i in range(length))

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.write("""
    <html><body>Python URL Shortening App</body></html>
    """)

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

      link = LinkMap(
        id = key,
        url = url,
        created = now
      )
      link.put()
      self.response.write("URL: %s\nShortn: %s" % (key, url) )
    else:
      self.response.write("Bad Request.")


class Serve(webapp2.RequestHandler):
  """ Redirects shortened to true URL """
  def get(self):
    if len(self.request.path.split('/')) > 1:
      key = self.request.path.split('/')[2]
      try:
        url = memcache.get(key)
      except:
        dbkey = ndb.Key(LinkMap, key)
        linkmap = dbkey.get()
        url = linkmap.url
      return self.redirect(str(url))

app = webapp2.WSGIApplication([
                             ('/', MainPage),
                             ('/s/.*', Shorten),
                             ('/r/.*', Serve)],
                             debug=True)
