import os

class Model(object):
    def __init__(self, configFile):
        if not os.path.isfile(configFile):
            raise IOError( "Config file not found at: " + configFile )
