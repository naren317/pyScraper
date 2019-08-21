import Constants as C
import re
import traceback
import time
from bs4 import BeautifulSoup as BS
from ResultDataModel import DataModel
from datetime import datetime as dt
from socket import timeout


STATUS_OK = 200

class PageParser:

       def __init__(self, keyword, resultURLs, requestSession, parseTags, sleepTimeBetweenResultURLs, pageParserType, urlFetchTimeout, urlHeaders, resultFileLocation):            
            self.Keyword = keyword
            self.ResultURLs = resultURLs
            self.RequestSession = requestSession
            self.ParseTags = parseTags
            self.ResultData = []
            self.EachURL = ''
            self.SleepTimeBetweenResultURLs = sleepTimeBetweenResultURLs
            self.PageParserType = pageParserType
            self.URLFetchTimeout = int(urlFetchTimeout)
            self.URLHeaders = urlHeaders
            self.ResultFileLocation = resultFileLocation

       def GetDataModelList(self):        
          try:
            
            for eachURL in self.ResultURLs:
             ModelElement = DataModel()
             try:

               if re.match(r'.*pdf', eachURL):
                   SessionConnection = self.RequestSession.get(eachURL, timeout= self.URLFetchTimeout, headers=self.URLHeaders)
                   if SessionConnection.status_code == STATUS_OK:                     
                     #time.sleep(self.SleepTimeBetweenResultURLs)               
                     PDFData = SessionConnection.content
                     with open(self.ResultFileLocation + dt.now().strftime("%d-%m-%Y_%H-%M-%S") + "_" + eachURL.split("/").pop(), 'wb+') as fp:
                       fp.write(PDFData)
                      
                   PageTextContent = ""
   
               else: 
                   PageTextContent = self.RequestSession.get(eachURL, timeout= self.URLFetchTimeout, headers=self.URLHeaders)
                   if PageTextContent.status_code == STATUS_OK:
                     #time.sleep(self.SleepTimeBetweenResultURLs)
                     PageTextContent = PageTextContent.text

                   else:
                     PageTextContent = ""

             except Exception as error:
               print(eachURL + " Exception : " + str(error))
               self.ResultURLs.remove(eachURL)
               continue

             except timeout:
               self.ResultURLs.remove(eachURL)
               continue
             print("Fetched URL : " + eachURL)
             PageTextContent = re.sub(C.FILTER_COMMENT_TAGS, '', PageTextContent)
             PageTextContent = re.sub(C.FILTER_IE_TAGS, '', PageTextContent)
             PageSoup = BS(PageTextContent, self.PageParserType)             
            
             if PageSoup.script is not None:             
                PageSoup.script.decompose() 

             PageTextContent = PageSoup.findAll(text=True)

             ModelElement.SetData(self.ParseTags[0], self.ResultURLs.index(eachURL))
             ModelElement.SetData(self.ParseTags[1], dt.now().strftime("%d-%m-%Y %HH-%MM-%SS"))
             ModelElement.SetData(self.ParseTags[2],''.join(re.findall(C.URL_EXTRACTION_REGEX,eachURL)))
             ModelElement.SetData(self.ParseTags[3], eachURL) 
             ModelElement.SetData(self.ParseTags[4], self.Keyword)

             for tag in self.ParseTags:
              if self.ParseTags.index(tag) > 4:               
               ModelElement.SetData(tag , self.DataSorting(tag, PageTextContent))               
             self.ResultData.append(ModelElement.GetDataModelList())
             time.sleep(self.SleepTimeBetweenResultURLs)
            return self.ResultData

          except Exception as error:
            print("Error while parsing URL data..." + "URLParsing.py- class PageParser - def GetData() : "+ traceback.format_exc())
            return self.ResultData
    
            
       def DataSorting(self, tag, pageTextContent):          
         try:
           tempDataList = []
           for element in pageTextContent:           

              if len(tag) > 0 and tag != 'content':
                 if element.parent.name == tag:
                    tempDataList.append(element)

              else:
                 if element.parent.name in ['style', 'script', '[document]', 'head', 'title','noscript']:
                   continue

                 #elif re.match('<!-.*->',str(element.encode('utf-8'))):
                 #  continue

                 else:
                   tempDataList.append(element)

           return ' '.join(tempDataList).strip().replace("\n\n"," ")

         except Exception as error:
            print("Error while sorting web page data..." + "URLParsing.py- class PageParser - def DataSorting) : "+ traceback.format_exc())
            return ""
