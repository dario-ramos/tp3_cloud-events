from google.appengine.ext import ndb
import event
import event_guest

class EventAttendance(ndb.Model)
    event = ndb.StructuredProperty(Event)
    eventGuest = ndb.StructuredProperty(EventGuest)
