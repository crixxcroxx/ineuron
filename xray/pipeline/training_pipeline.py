import sys

from xray.components.data_ingestion import DataIngestion
from xray.components.data_transformation import DataTransformation
from xray.components.model_training import ModelTrainer
from xray.entities.artifact_entity import DataIngestionArtifact, DataTranformationArtifact, ModelTrainerArtifact
from xray.entities.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
from xray.exception import XRayException
from xray.logger import logging


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_training_config = ModelTrainerConfig()

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
        
    def start_data_transformation(self,
                                  data_ingestion_artifact:DataIngestionArtifact) -> DataTranformationArtifact:
        logging.info("Entered start_data_transformation from training_pipeline")

        try:
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=self.data_transformation_config
            )

            data_transformation_artifact = data_transformation.initiate_data_transformation()

            logging.info("Exited start_data_transformation from training_pipeline")

            return data_transformation_artifact

        except Exception as e:
            raise XRayException(e, sys)
        
    def start_model_trainer(self,
                             data_transformation_artifact:DataTranformationArtifact) -> ModelTrainerArtifact:
        logging.info("Entered start_model_trainer from training_pipeline")

        try:
            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_training_config
            )

            model_trainer_artifact = model_trainer.initiate_model_training()

            logging.info("Exited start_model_trainer from training_pipeline")

            return model_trainer_artifact
        
        except Exception as e:
            raise XRayException(e, sys)
    
    def run_pipeline(self) -> None:
        logging.info("Entered run_pipeline from training_pipeline")

        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
            data_transformation_artifact:DataTranformationArtifact = self.start_data_transformation(
                data_ingestion_artifact=data_ingestion_artifact
            )
            model_trainer_artifact:ModelTrainerArtifact = self.start_model_trainer(
                data_transformation_artifact=data_transformation_artifact
            )

            logging.info("Exited the run_pipeline from training_pipeline")

        except Exception as e:
            raise XRayException(e, sys)
        