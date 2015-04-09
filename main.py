import webapp2
import datetime
import string
import random
import jinja2
import os
from models import LinkMap
from google.appengine.ext import ndb
from google.appengine.api import memcache


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
  def get(self):
    linkmaps = LinkMap.query().order(-LinkMap.created).fetch(50)
    template_values = {
    'linkmaps': linkmaps
    }
    template = JINJA_ENVIRONMENT.get_template('htdocs/index.html')
    self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)])
