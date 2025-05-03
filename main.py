import sys

from xray.exception import XRayException
from xray.pipeline.training_pipeline import TrainPipeline


def start_training():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    
    except Exception as e:
        raise XRayException(e, sys)


if __name__ == "__main__":
    start_training()

# =============
# import subprocess
# import os

# y = f"docker run --rm -it -v {os.path.expanduser('~')}/.aws:/root/.aws -v {os.getcwd()}:/aws feba658416e3 aws --version"

# try:
#     # x = subprocess.run(
#     #     ["docker", "run", "--rm", "-it", "-v", f"{os.path.expanduser('~')}/.aws:/root/.aws", "-v", f"{os.getcwd()}:/aws", "feba658416e3", "aws", "--version"],
#     #     capture_output=True,
#     #     text=True,
#     #     check=True
#     # )
#     x = os.system(y)
#     print("AWS Version:")
#     print(x.)
# except subprocess.CalledProcessError as e:
#     print(f"Error running AWS command:")
#     print(f"Return Code: {e.returncode}")
#     print(f"Stdout: {e.stdout}")
#     print(f"Stderr: {e.stderr}")  # Print the standard error
# except FileNotFoundError:
#     print("Error: 'docker' command not found.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")