import os
from dataclasses import dataclass, field

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


@dataclass
class DataTransformationConfig:
    color_jitter_transformation:dict = field(default_factory=lambda: {
        "brightness": BRIGHTNESS,
        "contrast": CONTRAST,
        "saturation": SATURATION,
        "hue": HUE
    })
    normalize_transforms:dict = field(default_factory=lambda: {
        "mean": NORMALIZE_LIST_1,
        "std": NORMALIZE_LIST_2
    })
    data_loader_params:dict = field(default_factory=lambda: {
        "batch_size": BATCH_SIZE,
        "shuffle": SHUFFLE,
        "pin_memory": PIN_MEMORY
    })
    artifact_dir:str = os.path.join(
        ARTIFACT_DIR, TIME_STAMP, "data_transformaion"
    )
    train_transforms_file:str = os.path.join(
        artifact_dir, TRAIN_TRANSFORMS_FILE
    )
    test_transforms_file:str = os.path.join(
        artifact_dir, TEST_TRANSFORMS_FILE
    )
    resize:int = RESIZE
    center_crop:int = CENTER_CROP
    random_rotation:int = RANDOM_ROTATION


@dataclass
class ModelTrainerConfig:
    artifact_dir:str = os.path.join(ARTIFACT_DIR, TIME_STAMP, "model_training")
    trained_bentoml_model_name:str = "xray_model"
    trained_model_path:str = os.path.join(artifact_dir, TRAINED_MODEL_NAME)
    train_transforms_key:str = TRAIN_TRANSFORMS_KEY
    epochs:int = EPOCH
    device:str = DEVICE
    optimizer_params:dict = field(default_factory=lambda: {
        "lr": 0.01,
        "momentum": 0.8
    })
    scheduler_params:dict = field(default_factory=lambda: {
        "step_size": STEP_SIZE,
        "gamma": GAMMA
    })
