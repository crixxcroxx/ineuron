import logging
import os

from xray.constants.training_pipeline import TIME_STAMP


LOG_FILE:str = f"{TIME_STAMP}.log"

logs_path = os.path.join(os.getcwd(), "logs", TIME_STAMP)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO
)