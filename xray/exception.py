import os
import sys


def error_message_detail(error: Exception, error_details: sys) -> str:
    _, _, exc_tb = error_details.exc_info()
    file_name:str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message:str = f"{file_name}, {exc_tb.tb_lineno}, {str(error)}"
    return error_message


class XRayException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)

        self.error_message:str = error_message_detail(
            error_message, error_detail
        )

    def __str__(self):
        return self.error_message