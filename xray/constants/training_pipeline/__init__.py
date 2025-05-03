from datetime import datetime
from typing import List

import torch


TIME_STAMP:datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACT_DIR:str = "artifacts"

BUCKET_NAME:str = "xraylungimgs001"

S3_DATA_FOLDER:str = "data"

CLASS_LABEL_1:str = "NORMAL"
CLASS_LABEL_2:str = "PNEUMONIA"