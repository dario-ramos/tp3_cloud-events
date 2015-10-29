#!/usr/bin/env python

from google.appengine.ext import ndb

class EventGuest(ndb.Model):
    firstName = ndb.StringProperty(indexed=False)
    lastName = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=True)
    company = ndb.StringProperty(indexed=False)
