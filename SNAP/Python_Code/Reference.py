#########################################################
# Py_Reference.py
#   - Custom functions for all named functions in SNAP datasets.
#
# These functions were moved into this file
#   for reuse and to reduce Notebook complexity.
#########################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

################################
        #2007 Datasets
################################

Unit_demo= pd.read_csv('./data/07_DataDict/UNIT_Demo.csv')
Unit_assets=pd.read_csv('./data/07_DataDict/UNIT_Assets.csv')
Unit_ExDed=pd.read_csv('./data/07_DataDict/UNIT_ExDed.csv')
Unit_Inc=pd.read_csv('./data/07_DataDict/UNIT_Inc.csv')
Pers_Char=pd.read_csv('./data/07_DataDict/PERS_Char.csv')
Pers_Inc=pd.read_csv('./data/07_DataDict/PERS_Inc.csv')

################################
        #2017 Datasets
################################

Unit_demo= pd.read_csv('./data/17_DataDict/UNIT_Demo.csv')
Unit_assets=pd.read_csv('./data/17_DataDict/UNIT_Assets.csv')
Unit_ExDed=pd.read_csv('./data/17_DataDict/UNIT_ExDed.csv')
Unit_Inc=pd.read_csv('./data/17_DataDict/UNIT_Inc.csv')
Pers_Char=pd.read_csv('./data/17_DataDict/PERS_Char.csv')
Pers_Inc=pd.read_csv('./data/17_DataDict/PERS_Inc.csv')

################################
    #Correlated Features
################################

corr_features = pd.read_csv("./data/corr_features.csv")
