from NetworkSecurity.exception.exception import CustomException
import logging
from NetworkSecurity.entity.config_entity import DataIngestionConfig
from NetworkSecurity.entity.artifact_entity import DataIngestionArtifact
import os
import sys
import pymongo
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


from dotenv import load_dotenv
load_dotenv()
Mongo_Db_url=os.getenv("Mongo_Db_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config=DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config

        except Exception as e:
            raise CustomException(e,sys)
    
    def export_collection_as_df(self):
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(Mongo_Db_url)
            collection=self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df.drop("_id",axis=1,inplace=True)
            df.replace({"na":np.nan},inplace=True)
            return df

        except Exception as e:
            raise CustomException(e,sys)
        
    def export_data_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_Store_file_path
            ##creating a folder
            dir_path=os.path.join(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path)
            return dataframe
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def split_data_as_train_test(self,dataframe=pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("performed split on data")
            logging.info("acquired traina and test data")

            
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            
        except Exception as e:
            raise CustomException(e,sys)
            
    
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_df()

            dataframe = self.export_data_feature_store(
                dataframe
            )
            data_ingestion_artifact = (
                self.split_data_as_train_test(
                    dataframe
                )
            )

            logging.info(
                "Data ingestion completed successfully"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)