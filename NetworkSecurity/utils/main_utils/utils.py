from NetworkSecurity.exception.exception import CustomException
from NetworkSecurity.logger.logger import logging
import os
import sys
import pickle
import yaml
#import dill
import numpy as np

def read_yaml_file(filepath:str)->dict:
    try:
        with open(filepath,'rb') as file:
          return  yaml.safe_load(file)
    except Exception as e:
        raise CustomException(e,sys)
    
def write_yaml_file(
    file_path: str,
    content: object,
    replace: bool = False
) -> None:
    try:
        # Get the directory where the YAML file will be stored
        directory = os.path.dirname(file_path)

        # Create the directory if it does not exist
        if directory:
            os.makedirs(directory, exist_ok=True)

        # If replace=True and the file already exists, remove it
        if replace and os.path.isfile(file_path):
            os.remove(file_path)

        # Write the YAML file
        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise CustomException(e, sys)