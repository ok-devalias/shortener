from google.appengine.ext import ndb

class LinkMap(ndb.Model):
  url = ndb.StringProperty(required=True)
  created = ndb.DateProperty()
