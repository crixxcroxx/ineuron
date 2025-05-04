import os
import sys
from xray.exception import XRayException


class S3Operation:
    def __init__(self):
        image_id = "feba658416e3"
        aws_config_path = os.path.join(os.path.expanduser('~'), '.aws')
        current_dir = os.getcwd()

        self.docker_command = f'docker run --rm --entrypoint "" -v {aws_config_path}:/root/.aws -v {current_dir}:/aws {image_id}'

    def sync_folder_to_s3(self, folder:str, bucket_name:str, bucket_folder_name:str) -> None:
        try:
            command:str = f"{self.docker_command} aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}"
            os.system(command)

        except Exception as e:
            raise XRayException(e, sys)
        
    def sync_folder_from_s3(self, folder:str, bucket_name:str, bucket_foder_name:str) -> None:
        try:
            command:str = f"{self.docker_command} aws s3 sync s3://{bucket_name}/{bucket_foder_name} {folder}"
            os.system(command)

        except Exception as e:
            raise XRayException(e, sys) 
        