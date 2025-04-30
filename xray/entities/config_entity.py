import os
from dataclasses import dataclass

from torch import device

from xray.constants.training_pipeline import *


@dataclass
class DataIngestionConfig:
    S3_data_folder:str = S3_DATA_FOLDER
    bucket_name:str = BUCKET_NAME
    artifact_dir:str = os.path.join(ARTIFACT_DIR, TIME_STAMP)
    data_path:str = os.path.join(artifact_dir, 
                                 "data_ingestion",
                                 S3_data_folder)
    train_data_path:str = os.path.join(data_path, "train")
    test_data_path:str = os.path.join(data_path, "test")