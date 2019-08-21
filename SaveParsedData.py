
import xlsxwriter as x
import traceback

from time import strftime

class SaveData:

      def __init__(self, fileSuffix, searchResultList, parsedTags, resultFileLocation):

           self.FileSuffix = fileSuffix
           self.SearchResultList = searchResultList
           self.ParsedTags = parsedTags
           self.ResultFileLocation = resultFileLocation

      def WriteData(self):
        try:
          row = col = 0
          wb = x.Workbook(self.ResultFileLocation + strftime("%d-%m-%Y_%H-%M-%S") + "_" + self.FileSuffix + ".xlsx")
          ws = wb.add_worksheet(strftime("%d-%m-%Y_%H-%M-%S"))
          

          for tag in self.ParsedTags:
            ws.write(row, col + self.ParsedTags.index(tag), tag)
          row += 1

          for modelElement in self.SearchResultList:
            for tag in self.ParsedTags:
              #if not tag in [self.ParsedTags[0], self.ParsedTags[1], self.ParsedTags[2], self.ParsedTags[3], self.ParsedTags[4]]:
               
#               if modelElement[self.ParsedTags.index(tag)][tag] is None:
               
#                 ws.write(row, col + self.ParsedTags.index(tag), "")
                 
#               else:
                
                ws.write(row, col + self.ParsedTags.index(tag), modelElement[self.ParsedTags.index(tag)][tag])
            row += 1
          print("Closing and saving result excelsheet: " + self.ResultFileLocation + strftime("%d-%m-%Y_%H-%M-%S") + "_" + self.FileSuffix + ".xlsx")
          wb.close()

        except Exception as error:
           print("Error while writing data to file..." + "SaveParsedData.py- class SaveData - def WriteData) : "+ traceback.format_exc())
          
