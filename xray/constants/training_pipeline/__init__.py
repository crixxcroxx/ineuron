from datetime import datetime
from typing import List

import torch


TIME_STAMP:datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

# data ingestion
ARTIFACT_DIR:str = "artifacts"
BUCKET_NAME:str = "xraylungimgs001"
S3_DATA_FOLDER:str = "data"


# data transformation
CLASS_LABEL_1:str = "NORMAL"
CLASS_LABEL_2:str = "PNEUMONIA"

BRIGHTNESS:float = 0.1
CONTRAST:float = 0.1
SATURATION:float = 0.1
HUE:float = 0.1
RESIZE:int = 224
CENTER_CROP:int = 224
RANDOM_ROTATION:int = 10
NORMALIZE_LIST_1:List[int] = [0.485, 0.456, 0.406]
NORMALIZE_LIST_2:List[int] = [0.229, 0.224, 0.225]
TRAIN_TRANSFORMS_KEY:str = "xray_train_transorms"
TRAIN_TRANSFORMS_FILE:str = "train_transforms.pkl"
TEST_TRANSFORMS_FILE:str = "test_transforms.pkl"
BATCH_SIZE:int = 2
SHUFFLE:bool = False
PIN_MEMORY:bool = True


# model training
TRAINED_MODEL_DIR:str = "trained_model"
TRAINED_MODEL_NAME:str = "model.pt"
DEVICE:str = torch.device("cuda" if torch.cuda.is_available() else "cpu")
STEP_SIZE:int = 6
GAMMA:float = 0.5
EPOCH:int = 3
