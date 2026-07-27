import os
import sys
from NetworkSecurity.exception.exception import CustomException
from NetworkSecurity.logger.logger import logging
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from NetworkSecurity.constant.training_pipeline import TARGET_COLUMN,DATA_TRANSFORMATION_IMPUTER_PARAMS
from NetworkSecurity.entity.artifact_entity import DataTransformationArtifact,DataValidationArtifact
from NetworkSecurity.utils.main_utils.utils import save_object,save_numpy_array_data
from NetworkSecurity.entity.config_entity import DataTransformationConfig
import numpy as np
import pandas as pd


class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,
                 data_tranformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_tranformation_config

        except Exception as e:
            raise CustomException(e,sys)
    ##reading the dataset:
    @staticmethod
    def read_data(filepath)->pd.Dataframe:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            raise CustomException(e,sys)
    @staticmethod
    def get_data_tranform()->Pipeline:
        """
        Args:
            cls:DataTransformation

        Return: 
            A pipeline object
        """
        logging.info("entered get_data_tranform method")
        try:
            KNN_imputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info("intialized KNN imputer")
            processor=Pipeline([("imputer",KNN_imputer)])
            return processor
        
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info("started the data initiaion step")
            train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            ##Removing the target variable:

            ##FOR THE TRAIN DATAFRAME
            input_feature_train_df=train_df.drop(TARGET_COLUMN,axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1, 0)

            ##FOR THE TEST DATAFRAME
            input_feature_test_df=test_df.drop(TARGET_COLUMN,axis=1)
            target_feature_test_df=test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1, 0)

            ## setting up the knn pipeline
            preprocessor=self.get_data_tranform()
            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature=preprocessor.transform(input_feature_train_df)
            transformed_input_test_feature =preprocessor_object.transform(input_feature_test_df)
             

            train_arr = np.c_[transformed_input_train_feature, np.array(target_feature_train_df) ]
            test_arr = np.c_[ transformed_input_test_feature, np.array(target_feature_test_df) ]

            ##save data in numpy array:
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array=test_arr)
            save_object(self.data_transformation_config.transformed_object_file_path,obj=preprocessor_object)

            ##preparing artifacts:
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact


            
        except Exception as e:
            raise CustomException(e,sys)