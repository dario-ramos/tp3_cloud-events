from abc import ABCMeta, abstractmethod
import event

class IEventRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, aName, aDate, aVacancies): pass

class EventRepository(IEventRepository):
    def create(self, aName, aDate, aVacancies):
        newEvent = event.Event(
            name = aName,
            date = aDate,
            vacancies = aVacancies
        )
        newEvent.put()
