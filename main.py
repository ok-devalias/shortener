import webapp2
import datetime
import string
import random
from google.appengine.ext import ndb
from google.appengine.api import memcache



class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.write("""
    <html><body>Python URL Shortening App</body></html>
    """)


app = webapp2.WSGIApplication([('/', MainPage)])
