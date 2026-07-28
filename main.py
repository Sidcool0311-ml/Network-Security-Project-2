from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.logger.logger import logging
from NetworkSecurity.exception.exception import CustomException
import sys
from NetworkSecurity.entity.config_entity import DataValidationConfig
from NetworkSecurity.components.data_validation import DataValidation
from NetworkSecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig,
  
)
from NetworkSecurity.components.data_transformation import DataTransformation
from NetworkSecurity.entity.config_entity import DataTransformationConfig
from NetworkSecurity.components.model_trainer import ModelTrainer
from NetworkSecurity.entity.config_entity import ModelTrainerConfig



if __name__ == "__main__":

    try:

        logging.info("Starting the data ingestion pipeline")

        trainingpipelineconfig = TrainingPipelineConfig()

        data_ingestion_config = DataIngestionConfig(
            trainingpipelineconfig
        )

        data_ingestion = DataIngestion(
            data_ingestion_config
        )

        logging.info("Initiating the data ingestion")

        dataingestionartifact = (
            data_ingestion.initiate_data_ingestion()
        )

        logging.info(
            "Data ingestion completed successfully"
        )

        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(data_validation_config,dataingestionartifact)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")

        
        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
        

    except Exception as e:
        raise CustomException(e, sys)