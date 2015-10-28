import configuration
import login_manager
import event_repository

class Model(object):
    def __init__(self, configFile):
        self.config = configuration.Configuration(configFile)
        if( self.config.getProperty("mock_db") == "1" ):
            self.loginManager = login_manager.MockLoginManager()
            self.eventRepository = event_repository.MockEventRepository()
        else:
            self.loginManager = login_manager.LoginManager()
            self.eventRepository = event_repository.EventRepository()

    def getLoginManager(self):
        return self.loginManager

    def getEventRepository(self):
        return self.eventRepository
