#import polars as pl
import pandas as pd
import os
import numpy as np
from collections import namedtuple

from kaggle_titanic_repo_example.__competition__ import COMP_NAME, TRAIN_NAME, \
    TEST_NAME, ID_COLUMN_NAME, SUB_NAME

def load_data(data_path = f'/kaggle/input/{COMP_NAME}'):
    train = pd.read_csv(os.path.join(data_path, 
                                     TRAIN_NAME),
                        index_col=ID_COLUMN_NAME)
    comp = pd.read_csv(os.path.join(data_path, 
                                    TEST_NAME),
                       index_col=ID_COLUMN_NAME)
    sub = pd.read_csv(os.path.join(data_path, 
                                   SUB_NAME))
    Data = namedtuple('Data', ['train',
                               'comp',
                               'sub'])
    return Data(train, 
                comp, 
                sub)


                
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
ct=ColumnTransformer([('impute', 
                       SimpleImputer(strategy='mean'), 
                       ['Age', 'Fare']),
                      ('encode', 
                       OneHotEncoder(handle_unknown='ignore',
                                    sparse_output=False), 
                       ['Sex']),
                     ],
                     remainder='drop')
preprocessing_pipeline = Pipeline([('prep', ct),
                                   ('scale', PowerTransformer()),
                                  ]).set_output(transform='pandas')
