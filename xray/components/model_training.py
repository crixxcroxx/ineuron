import os
import sys

import bentoml
import joblib
import torch
import torch.nn.functional as F
from torch.nn import Module
from torch.optim import Optimizer
from torch.optim.lr_scheduler import StepLR, _LRScheduler
from tqdm import tqdm

from xray.constants.training_pipeline import *
from xray.entities.artifact_entity import DataTranformationArtifact, ModelTrainerArtifact
from xray.entities.config_entity import ModelTrainerConfig
from xray.exception import XRayException
from xray.logger import logging
from xray.ml.model.arch import Net


class ModelTrainer:
    def __init__(self,
                 data_transformation_artifact:DataTranformationArtifact,
                 model_trainer_config:ModelTrainerConfig):
        self.model_trainer_config:ModelTrainerConfig = model_trainer_config
        self.data_transformation_artifact:DataTranformationArtifact = data_transformation_artifact
        self.model:Module = Net()

    def train(self, optimizer:Optimizer) -> None:
        try:
            logging.info("Entered train from model_training")

            self.model.train()

            pbar = tqdm(self.data_transformation_artifact.transformed_train_object)

            correct:int = 0
            processed:int = 0

            for batch_idx, (data, target) in enumerate(pbar):
                data, target = data.to(self.model_trainer_config.device), target.to(self.model_trainer_config.device)

                optimizer.zero_grad()
                y_pred = self.model(data)
                loss = F.nll_loss(y_pred, target) # negative log likelihood
                loss.backward()

                pred = y_pred.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().item()
                processed += len(data)

                pbar.set_description(
                    desc=f"Loss={loss.item()} | Batch ID={batch_idx} | Accuracy={100.0 * correct / processed:0.2f}"
                )

            logging.info("Exited train loop from model_training")
            
        except Exception as e:
            raise XRayException(e, sys)
        
    def test(self) -> None:
        try:
            logging.info("Entered test from model_training")

            self.model.eval()

            test_loss:float = 0.0
            correct:int = 0

            with torch.inference_mode():
                for(data, target) in self.data_transformation_artifact.transformed_test_object:
                    data, target =  data.to(self.model_trainer_config.device), target.to(self.model_trainer_config.device)

                    output = self.model(data)
                    test_loss += F.nll_loss(output, target, reduction="sum").item()
                    pred = output.argmax(dim=1, keepdim=True)
                    correct += pred.eq(target.view_as(pred)).sum().item()
                
                test_loss /= len(self.data_transformation_artifact.transformed_test_object.dataset)

                res = f"Average Loss={test_loss:.4f} | \
                    Accuracy={100.0 * correct / len(self.data_transformation_artifact.transformed_test_object.dataset)}"
                
            logging.info(f"Test result: {res}")
        
        except Exception as e:
            raise XRayException(e, sys)
        
    def initiate_model_training(self) -> ModelTrainerArtifact:
        try:
            logging.info("Entered initiate_model_training from model_training")

            model:Module = self.model.to(self.model_trainer_config.device)
            optimizer:Optimizer = torch.optim.SGD(model.parameters(), **self.model_trainer_config.optimizer_params)
            scheduler:_LRScheduler = StepLR(
                optimizer=optimizer, **self.model_trainer_config.scheduler_params
            )

            for epoch in range(1, self.model_trainer_config.epochs + 1):
                print("Epoch: ", epoch)

                self.train(optimizer=optimizer)

                optimizer.step()
                scheduler.step()

                self.test()

            os.makedirs(self.model_trainer_config.artifact_dir, exist_ok=True)
            torch.save(model, self.model_trainer_config.trained_model_path)

            train_transforms_obj = joblib.load(self.data_transformation_artifact.train_transform_file_path)

            bentoml.pytorch.save_model(
                name=self.model_trainer_config.trained_bentoml_model_name,
                model=model,
                custom_objects={
                    self.model_trainer_config.train_transforms_key: train_transforms_obj
                }
            )

            model_trainer_artifact:ModelTrainerArtifact = ModelTrainerArtifact(
                trained_model_path=self.model_trainer_config.trained_model_path
            )

            logging.info("Exited initiate_model_training from model_training")

            return model_trainer_artifact

        except Exception as e:
            raise XRayException(e, sys)
