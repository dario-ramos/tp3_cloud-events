#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from google.appengine.ext import ndb
from google.appengine.ext import db
import event
from event import Event

class IEventRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, aName, aDate, aVacancies): pass
    def getAll(self): pass
    def getByName(self, eventID): pass
    def update( self, event ): pass

class EventRepository(IEventRepository):
    def create(self, aName, aDate, aVacancies):
        newEvent = Event( parent = event.eventKey() )
        newEvent.name = aName
        newEvent.date = aDate
        newEvent.vacancies = aVacancies
        newEvent.put()

    def getAll(self):
        return Event.query().fetch(900) #TODO Don't hardcode

    def getByName(self, eventID):
        #Alternative 1
        #q = db.Query(Event)
        #return q.filter( "name =", eventID ).fetch(1)

        #Alternative 2
        #return db.GqlQuery('SELECT * FROM Event WHERE name = :1', eventID).fetch(1)
        
        #Alternative 3
        #q = Event.query(ancestor = event.eventKey())
        #return q.filter( "name =", eventID ).fetch(1)
        #return q.filter(ndb.GenericProperty("name") != eventID).get()
        
        #TODO This is inefficient; make one of the aboe work
        eventList = self.getAll()
        for event in eventList:
            if event.name == eventID:
                return event
        return None

    def update( self, event ):
        event.put()
