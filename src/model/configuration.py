#!/usr/bin/env python

import os


class Configuration:

    def __init__(self, configFile):
        if not os.path.isfile(configFile):
            raise IOError("Config file not found at: " + configFile)
        fileLines = []
        with open(configFile) as f:
            fileLines = f.readlines()
        self.keys = {}
        for line in fileLines:
            if not line:
                continue
            if line[0] == "#":
                continue
            keyAndValue = line.split("=")
            if len(keyAndValue) != 2:
                continue
            self.keys[keyAndValue[0].strip()] = keyAndValue[1].strip()

    def getProperty(self, propName):
        return self.keys[propName]
