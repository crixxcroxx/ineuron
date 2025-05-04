import os
import sys
from typing import Tuple

import joblib
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets import ImageFolder

from xray.entities.config_entity import DataTransformationConfig
from xray.entities.artifact_entity import DataIngestionArtifact, DataTranformationArtifact
from xray.exception import XRayException
from xray.logger import logging


class DataTransformation:
    def __init__(self,
                 data_transformation_config:DataTransformationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifact = data_ingestion_artifact
    
    def transform_train_data(self) -> transforms.Compose:
        try:
            logging.info("Entered transform_train_data from data_transformation")

            train_transform:transforms.Compose = transforms.Compose([
                transforms.Resize(self.data_transformation_config.resize),
                transforms.CenterCrop(self.data_transformation_config.center_crop),
                transforms.ColorJitter(**self.data_transformation_config.color_jitter_transformation),
                transforms.RandomHorizontalFlip(),
                transforms.RandomRotation(self.data_transformation_config.random_rotation),
                transforms.ToTensor(),
                transforms.Normalize(**self.data_transformation_config.normalize_transforms)
            ])

            logging.info("Exited transform_train_data from data_transformation")

            return train_transform
        
        except Exception as e:
            raise XRayException(e, sys)

    def transform_test_data(self) -> transforms.Compose:
        try:
            logging.info("Entered transform_test_data from data_transformation")

            test_transform:transforms.Compose = transforms.Compose([
                transforms.Resize(self.data_transformation_config.resize),
                transforms.CenterCrop(self.data_transformation_config.center_crop),
                transforms.ToTensor(),
                transforms.Normalize(**self.data_transformation_config.normalize_transforms)
            ])

            logging.info("Exited transform_test_data from data_transformation")

            return test_transform
        
        except Exception as e:
            raise XRayException(e, sys)
        
    def data_loader(self,
                    train_transform:transforms.Compose,
                    test_transform:transforms.Compose) -> Tuple[DataLoader, DataLoader]:
        try:
            logging.info("Entered data_loader from data_transformation")

            train_data:Dataset = ImageFolder(
                os.path.join(self.data_ingestion_artifact.train_file_path),
                transform = train_transform
            )

            test_data:Dataset = ImageFolder(
                os.path.join(self.data_ingestion_artifact.test_file_path),
                transform = test_transform
            )

            logging.info("Created train and test data paths")

            train_loader:DataLoader = DataLoader(
                train_data, **self.data_transformation_config.data_loader_params
            )

            test_loader:DataLoader = DataLoader(
                test_data, **self.data_transformation_config.data_loader_params
            )

            logging.info("Exited data_loader from data_transformation")

            return train_loader, test_loader
        
        except Exception as e:
            raise XRayException(e, sys)
        
    def initiate_data_transformation(self) -> DataTranformationArtifact:
        try:
            logging.info("Entered initiate_data_transformation from data_transformation")

            train_transform:transforms.Compose = self.transform_train_data()
            test_transform:transforms.Compose = self.transform_test_data()

            os.makedirs(self.data_transformation_config.artifact_dir, exist_ok=True)

            joblib.dump(
                train_transform, self.data_transformation_config.train_transforms_file
            )
            joblib.dump(
                test_transform, self.data_transformation_config.test_transforms_file
            )

            train_loader, test_loader = self.data_loader(
                train_transform, test_transform
            )

            data_transformation_artifact:DataTranformationArtifact = DataTranformationArtifact(
                transformed_train_object=train_loader,
                transformed_test_object=test_loader,
                train_transform_file_path=self.data_transformation_config.train_transforms_file,
                test_transform_file_path=self.data_transformation_config.test_transforms_file
            )

            logging.info("Exited initiate_data_transformation from data_transformation")

            return data_transformation_artifact
        
        except Exception as e:
            raise XRayException(e, sys)
        