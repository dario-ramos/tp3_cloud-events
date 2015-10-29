from google.appengine.ext import ndb
from event import Event
from event_guest import EventGuest

class EventAttendance(ndb.Model):
    event = ndb.StructuredProperty(Event)
    eventGuest = ndb.StructuredProperty(EventGuest)
