from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.logger.logger import logger
from NetworkSecurity.exception.exception import CustomException
import sys

from NetworkSecurity.entity.config_entity import (
    DataIngestionConfig,
    TrainingPipelineConfig
)


if __name__ == "__main__":

    try:

        logger.info("Starting the data ingestion pipeline")

        trainingpipelineconfig = TrainingPipelineConfig()

        data_ingestion_config = DataIngestionConfig(
            trainingpipelineconfig
        )

        data_ingestion = DataIngestion(
            data_ingestion_config
        )

        logger.info("Initiating the data ingestion")

        dataingestionartifact = (
            data_ingestion.initiate_data_ingestion()
        )

        logger.info(
            "Data ingestion completed successfully"
        )

        print(dataingestionartifact)

    except Exception as e:

        logger.exception(
            "Error occurred during data ingestion"
        )

        raise CustomException(e, sys)