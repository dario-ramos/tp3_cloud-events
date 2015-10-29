#!/usr/bin/env python

from google.appengine.ext import ndb


class EventAttendance(ndb.Model):
    eventName = ndb.StringProperty(indexed=False)
    guestEmail = ndb.StringProperty(indexed=False)
