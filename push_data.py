
import os
import sys
import json
import pymongo

from dotenv import load_dotenv
load_dotenv()
mongo_db_url=os.getenv("Mongo_Db_URL")
print(mongo_db_url)


import certifi
##this library provides tested collection of SSL/TSL root certificates.It helps python to verify that it is connecting to a secured https website.
import pandas as pd
import numpy as np
from NetworkSecurity.logger.logger import logger
from NetworkSecurity.exception.exception import CustomException

class NetworkDataExtract:
    def __init__(self):
        pass

    def csv_to_json_convertor(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())

            return records
         
        except Exception as e:
            raise CustomException(e,sys)
    
    def insert_data_mongoDB(self,records,database,collection):
        try:
            self.records=records
            self.database=database
            self.collection=collection
            
            
            ca = certifi.where()

            self.mongo_client = pymongo.MongoClient(
             mongo_db_url,
             tlsCAFile=ca
)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__':
    FILE_PATH="Network_DATA/phisingData.csv"
    DATABASE="SIDCOOL"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(filepath=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongoDB(records,DATABASE,Collection)
    print(no_of_records)
