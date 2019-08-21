
import traceback

class DataModel:

      def __init__(self):
          self.dataPairList = []

      def SetData(self, tag, data):
        try:
          self.dataPairList.append({tag:data})        
      
        except Exception as error:
          print("Error while setting data model..." + "ResultDataModel.py- class DataModel - def SetData) : "+ traceback.format_exc())

      def GetDataModelList(self):
        try:
             return self.dataPairList

        except Exception as error:
          print("Error while getting data model..." + "ResultDataModel.py- class DataModel - def GetDataModel) : "+ traceback.format_exc())
          return self.dataPairList 
