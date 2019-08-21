
import requests as r
import traceback
from googlesearch import search

class SearchEngineHandler:


      def __init__(self, proxies, topLevelDomain, numberOfResults, searchInterval, keyword, gSearchLang):

           self.Proxies = proxies
           self.Keyword = keyword
           self.TopLevelDomain = topLevelDomain
           self.NumberOfResults = numberOfResults
           self.SearchInterval = searchInterval
           self.GSearchLang = gSearchLang


      def InitiateSearch(self):
        try:
          session = r.Session()
          session.proxies = self.Proxies
          return (list(search(self.Keyword, tld=self.TopLevelDomain, lang=self.GSearchLang, num=self.NumberOfResults, stop=self.NumberOfResults, pause=self.SearchInterval)), session)

        except Exception as error:
          print("Error while Googling..." + "SearchEngine.py- class SearchEngineHandler - def InitiateSearch) : "+ traceback.format_exc())
          return ("","")   


