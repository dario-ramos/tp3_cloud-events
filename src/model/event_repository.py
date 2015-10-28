from abc import ABCMeta, abstractmethod
import os

class IEventRepository:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self, name, date, vacancies): pass

class MockEventRepository(IEventRepository):
    FIELD_SEPARATOR = "|"
    def __init__(self):
        self.repoFileName = os.path.dirname( os.path.abspath(__file__) ) + os.path.sep + "events.txt"

    def create(self, name, date, vacancies):
        with open( self.repoFileName, "a+" ) as textFile:
            textFile.write( name % FIELD_SEPARATOR % date % vacancies )

class EventRepository(IEventRepository):
    def create(self, name, date, vacancies):
        raise NotImplementedError()
