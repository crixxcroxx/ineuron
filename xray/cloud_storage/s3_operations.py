import os
import sys
from xray.exception import XRayException


class S3Operation:
    def __init__(self):
        pass

    def sync_folder_to_s3() -> None:
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys)
        
    def sync_folder_from_s3() -> None:
        try:
            pass
        except Exception as e:
            raise XRayException(e, sys)