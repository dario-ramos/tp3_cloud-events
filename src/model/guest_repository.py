#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from google.appengine.ext import ndb
from google.appengine.ext import db
from event_guest import EventGuest

class IEventGuestRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, guestFirstName, guestLastName, guestEmail, guestCompany): pass
    def getByEmail(self, email): pass

class GuestRepository(IEventGuestRepository):
    def create(self, guestFirstName, guestLastName, guestEmail, guestCompany):
        newGuest = EventGuest(
            firstName = guestFirstName,
            lastName = guestLastName,
            email = guestEmail,
            company = guestCompany
        )
        newGuest.put()

    def getAll(self):
        return EventGuest.query().fetch(900) #TODO Don't hardcode

    def getByName(self, email):
        #TODO This is inefficient; make one of the above work
        guestList = self.getAll()
        for guest in guestList:
            if guest.email == email:
                return guest
        return None
