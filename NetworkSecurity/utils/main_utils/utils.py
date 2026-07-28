from NetworkSecurity.exception.exception import CustomException
from NetworkSecurity.logger.logger import logging
import os
import sys
import pickle
import yaml
#import dill
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

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

def load_object(filepath:str)->object:
    try:
        if not os.path.exists(filepath):
            raise Exception("path does not exist")
        with open(filepath,"rb") as file:
            return pickle.load(file)
    except Exception as e:
        raise CustomException(e,sys)

def load_numpy_array_data(filepath)->object:
    try:
        with open(filepath,"rb") as file:
            return np.load(file)
    except Exception as e:
        raise CustomException(e,sys)

def evaluate_models(X_train,X_test,y_train,y_test,models,param):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs=GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report


    except Exception as e:
        raise CustomException(e,sys)