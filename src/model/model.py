import configuration
import login_manager

class Model(object):
    def __init__(self, configFile):
        self.config = configuration.Configuration(configFile)
        if( self.config.getProperty("mock_db") == "1" ):
            self.loginManager = login_manager.MockLoginManager()
        else:
            self.loginManager = login_manager.LoginManager()
    
    def getLoginManager(self):
        return self.loginManager

