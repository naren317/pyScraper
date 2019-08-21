
import sys as s
import traceback
from json import loads

class ConfigurationHandler:

    def __init__(self, configurationFile):

        self.configFile  = configurationFile 

    def ConfigurationParameters(self):

      try:       
        with open(self.configFile , 'r') as f:
              
              return loads(''.join(['{',f.read().split("%").pop(),'}']))
                 
      except Exception as error:
             print("Error while loading configuration..." + "Configuration.py- class ConfigurationHandler - def ConfigurationParameters) : "+ traceback.format_exc())
             s.exit() 
