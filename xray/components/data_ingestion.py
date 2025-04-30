import sys

from xray.cloud_storage.s3_operations import S3Operation
# from xray.constant.training_pipeline import *
from xray.entities.artifact_entity import DataIngestionArtifact
from xray.entities.config_entity import DataIngestionConfig
from xray.exception import XRayException
from xray.logger import logging


class DataIngestion:
    def __init__(self):
        pass

    def get_data_from_s3(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys)
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys)