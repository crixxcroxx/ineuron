import sys

from xray.cloud_storage.s3_operations import S3Operation
# from xray.constant.training_pipeline import *
from xray.entities.artifact_entity import DataIngestionArtifact
from xray.entities.config_entity import DataIngestionConfig
from xray.exception import XRayException
from xray.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.s3 = S3Operation()

    def get_data_from_s3(self):
        try:
            logging.info("Entered get_data_from_s3 from data_ingestion")
            
            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_foder_name=self.data_ingestion_config.S3_data_folder
            )

            logging.info("Exited get_data_from_s3 from data_ingestion")

        except Exception as e:
            raise XRayException(e, sys)
        
    def initiate_data_ingestion(self):
        logging.info("Entered the initiate_data_ingestion from data_ingestion")

        try:
            self.get_data_from_s3()

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path = self.data_ingestion_config.train_data_path,
                test_file_path =self.data_ingestion_config.test_data_path
            )

            logging.info("Entered initiate_data_ingestino from data_ingestion")

            return data_ingestion_artifact

        except Exception as e:
            raise XRayException(e, sys)