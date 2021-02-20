# Description: Handles json files
# Author: Jacob Maughan

# Sys Imports
from os import path
import json

class JsonHandler():
    def __init__(self, file):
        # Init | Creates file if needed
        self.file = file
    
    # Get the data from json file
    def getJson(self):
        with open(self.file) as tmpFile:
            return json.load(tmpFile)
    
    # Save the data to json file
    def saveJson(self, data):
        with open(self.file, 'w') as tmpFile:
            json.dump(data, tmpFile, indent=4)