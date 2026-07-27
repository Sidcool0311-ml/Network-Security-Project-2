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
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        directory = os.path.dirname(file_path)

        print("FILE PATH:", file_path)
        print("DIRECTORY:", directory)
        print("FILE EXISTS:", os.path.isfile(file_path))
        print("IS DIRECTORY:", os.path.isdir(file_path))

        os.makedirs(directory, exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        print("ERROR:", e)
        raise CustomException(e, sys)
def save_numpy_array_data(filepath:str,array:np.array):
    try:
        dir_path=os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        with open(filepath,"wb") as file_obj:
            np.save(file_obj,array)
    
    except Exception as e:
        raise CustomException(e,sys)
def save_object(filepath:str,obj:object)->None:
    try:
        logging.info("entered the save_object method of main.utils class")
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath,"wb") as file:
            pickle.dump(obj,file)
        logging.info("pickle file loaded")
    except Exception as e:
        raise CustomException(e,sys)