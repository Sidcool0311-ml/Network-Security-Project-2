##estimator.py will give the details about all info. that is present for the model
from NetworkSecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
import os
import sys 
from NetworkSecurity.exception.exception import CustomException
from NetworkSecurity.logger.logger import logging

class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            self.model=model
            self.preprocessor=preprocessor

        except Exception as e:
            raise CustomException(e,sys)
    def predict(self,X):
        try:
            X_transform=self.preprocessor.transform(X)
            y_hat=self.model.predict(X_transform)
            return y_hat
        except Exception as e :
            raise CustomException(e,sys)