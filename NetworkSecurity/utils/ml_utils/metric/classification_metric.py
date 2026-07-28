from NetworkSecurity.entity.artifact_entity import ClassifcationMetricArtifact
from sklearn.metrics import f1_score,recall_score,precision_score
from NetworkSecurity.exception.exception import CustomException
import sys


def get_classification_score(y_true,y_pred)->ClassifcationMetricArtifact:
    try:
        model_f1_score=f1_score(y_true,y_pred)
        model_recall_score=recall_score(y_true,y_pred)
        model_precision_score=precision_score(y_true,y_pred)

        classification_metric=ClassifcationMetricArtifact(f1_score=model_f1_score,
                                                          recall_score=model_recall_score,
                                                          precision_score=model_precision_score)
        return classification_metric
    except Exception as e:
        raise CustomException(e,sys)