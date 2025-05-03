import sys

from xray.components.data_ingestion import DataIngestion
from xray.entities.artifact_entity import DataIngestionArtifact
from xray.entities.config_entity import DataIngestionConfig
from xray.exception import XRayException
from xray.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered start_data_ingestion from training_pipeline")

        try:
            logging.info("Getting data from S3 bucket")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from S3")
            
            logging.info("Exited start_data_ingestion from training_pipeline")

            return data_ingestion_artifact

        except Exception as e:
            raise XRayException(e, sys)
    
    def run_pipeline(self) -> None:
        logging.info("Entered run_pipeline from training_pipeline")

        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()

            logging.info("Exited the run_pipeline from training_pipeline")

        except Exception as e:
            raise XRayException(e, sys)
        