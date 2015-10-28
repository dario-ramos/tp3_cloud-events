from google.appengine.ext import ndb

class Event(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    date = ndb.StringProperty(indexed=False)
    vacancies = ndb.IntegerProperty(indexed=False)
