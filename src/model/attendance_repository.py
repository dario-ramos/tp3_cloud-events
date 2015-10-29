from abc import ABCMeta, abstractmethod
from google.appengine.ext import ndb
from google.appengine.ext import db
import event
from event_attendance import EventAttendance

class IAttendanceRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, guestEmail, eventName): pass
    def getByEventNameAndGuestEmail(self, eventName, guestEmail): pass
    def deleteByEventNameAndGuestEmail(self, eventName, guestEmail): pass

class AttendanceRepository(IAttendanceRepository):
    def create(self, theGuestEmail, theEventName):
        newAttendance = EventAttendance(
            guestEmail = theGuestEmail,
            eventName = theEventName
        )
        newAttendance.put()

    def getAll(self):
        return EventAttendance.query().fetch(900) #TODO Don't hardcode

    def getByEventNameAndGuestEmail(self, eventName, guestEmail):
        #TODO This is inefficient, mae query.filter() work
        attendanceList = self.getAll()
        for attendance in attendanceList:
            if attendance.eventName == eventName and attendance.guestEmail == guestEmail:
                return attendance
        return None

    def deleteByEventNameAndGuestEmail(self, eventName, guestEmail):
        attendance = self.getByEventNameAndGuestEmail(eventName, guestEmail)
        if attendance is not None:
            attKey = db.Key.from_path(attendance.eventName, attendance.guestEmail)
            db.delete(attKey)
