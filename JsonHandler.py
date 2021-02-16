# Description: Handles json files
# Author: Jacob Maughan

# Sys Imports
import json
from os import path

class JsonHandler():
    def __init__(self, file, mainLine=""):
        # Init | Creates file if needed
        self.file = file
        if not path.exists(self.file):
            data = {}
            if not mainLine == "":
                data[mainLine] = []
            with open(self.dataFile, 'w') as tmpFile:
                json.dump(data, tmpFile, indent=4)
    
    # Get the data from json file
    def getJson(self):
        with open(self.file) as tmpFile:
            return json.load(tmpFile)
    
    # Save the data to json file
    def saveJson(self, data):
        with open(self.file, 'w') as tmpFile:
            json.dump(data, tmpFile, indent=4)