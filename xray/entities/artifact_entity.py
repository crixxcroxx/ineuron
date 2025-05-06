from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader


@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str


@dataclass
class DataTranformationArtifact:
    transformed_train_object:DataLoader
    transformed_test_object:DataLoader
    
    train_transform_file_path:str
    test_transform_file_path:str


@dataclass
class ModelTrainerArtifact:
    trained_model_path:str 
