from google.appengine.ext import ndb

class EventGuest(ndb.Model)
    firstName = ndb.StringProperty(indexed=False)
    LastName = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    company = ndb.StringProperty(indexed=False)
