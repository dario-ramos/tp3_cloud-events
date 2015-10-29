#!/usr/bin/env python

from google.appengine.ext import ndb

DEFAULT_EVENT_NAME = 'default_event'


def eventKey(event_name=DEFAULT_EVENT_NAME):
    return ndb.Key('Event', event_name)


class Event(ndb.Model):
    name = ndb.StringProperty(indexed=False)
    date = ndb.StringProperty(indexed=False)
    vacancies = ndb.IntegerProperty(indexed=False)
