#!/usr/bin/env python3

_CONFIGURATION_FILE_ = "parserConfig.config"

import sys as s
import traceback
from ConfigurationReader import ConfigurationHandler
from SearchEngine import SearchEngineHandler
from URLDataParsing import PageParser
from SaveParsedData import SaveData


class MainHandler:

      def __init__(self):

         if len(s.argv) > 1:
          self.Keyword = s.argv[1]

         else:
          self.Keyword = ""

      def ConfigurationReaderModule(self):
 
         return ConfigurationHandler(_CONFIGURATION_FILE_).ConfigurationParameters()

      def SearchEngineModule(self, config):
         if not self.Keyword:
            self.Keyword = config["DefaultSearchKeyword"]
         return SearchEngineHandler(config["Proxy"],config["TopLevelDomain"],config["NumberOfResults"],config["GoogleSearchInterval"],  self.Keyword, config["GoogleSearchLanguage"]).InitiateSearch()

      def URLDataParsingModule(self, scrapeURL, requestSession, parseTags, sleepTimeBetweenResultURLs, pageParserType, urlFetchTimeout, urlHeaders, resultFileLocation):
        
            return PageParser(self.Keyword, scrapeURL, requestSession, parseTags, sleepTimeBetweenResultURLs, pageParserType, urlFetchTimeout, urlHeaders, resultFileLocation).GetDataModelList()

      def SaveParsedDataModule(self, resultFileSuffix, resultModelList, parseTags, resultFileLocation):
             
            return SaveData(resultFileSuffix, resultModelList, parseTags, resultFileLocation).WriteData()


try:

  if __name__ == "__main__":

   MainInstanceHandler = MainHandler()

   Config = MainInstanceHandler.ConfigurationReaderModule()

   (ResultURLs, RequestSession) = MainInstanceHandler.SearchEngineModule(Config)

   if len(ResultURLs) == 0 :
      raise Exception('Google search failed....!!')

   ResultModelList = MainInstanceHandler.URLDataParsingModule(ResultURLs, RequestSession, Config["ParseTags"], Config["SleepTimeBetweenResultURLs"], Config["PageParserType"], Config["URLFetchTimeout"], Config["URLHeaders"], Config["ResultFileLocation"])

   MainInstanceHandler.SaveParsedDataModule(Config["ResultFileSuffix"], ResultModelList, Config["ParseTags"], Config["ResultFileLocation"])

except Exception as error:

   print("Error executing main ..." + "Scraper.py -  __main__) : "+ traceback.format_exc())
   s.exit()
