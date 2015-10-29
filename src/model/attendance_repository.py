from abc import ABCMeta, abstractmethod
from google.appengine.ext import ndb
from google.appengine.ext import db
import event
from event_attendance import EventAttendance

class IAttendanceRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, guest, event): pass

class AttendanceRepository(IAttendanceRepository):
    def create(self, eventGuest, theEvent):
        newAttendance = EventAttendance(
            eventGuest = eventGuest,
            event = theEvent
        )
        newAttendance.put()
