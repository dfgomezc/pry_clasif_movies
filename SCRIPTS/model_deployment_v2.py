#!/usr/bin/python

import numpy as np
import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.utils import class_weight
from sklearn import preprocessing
import time
import sys
import pandas as pd
import os
# Modelado
# ==============================================================================
from sklearn.neural_network import MLPRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import KFold
from sklearn import set_config
import multiprocessing
from joblib import dump, load
import json
import re


def transformar(Plot):
    vectorizer = load('../OUTPUT/MODELS/modelo_base_cv.bin')
    transformado = vectorizer.transform([Plot])
    return transformado


def predict_price(Plot):
    
    X_test_transformed = transformar(Plot)
    model = load('../OUTPUT/MODELS/modelo_base.bin')
    le = load('../OUTPUT/MODELS/modelo_base_le.bin')
    y_pred = model.predict(X_test_transformed)
    
    # resultado = pd.DataFrame(data=np.column_stack((le.classes_,y_pred[0])),columns=['Género','Probabilidad'])
    dictionary = dict(zip(le.classes_, y_pred[0]))
    
    return dictionary

Plot = "asdaASD SDFSDF sdfgsdf FDGDFG dfgdfg opdfgdfgljl SDFGDFG"


if __name__ == "__main__":
    
    if len(sys.argv) <= 0:
        print("Please add description of movie")
        
    else:

        Plot = int(sys.argv[1])
        p1 = predict_price(Plot)
        
        print(f"{Plot}")
        print('Probabilidad de pertencer a un género ', p1)
        
        
        
