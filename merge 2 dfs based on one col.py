# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:48:35 2022

@author: Omnia
"""

import os
import cv2
import pandas as pd


df1 = pd.read_csv(r".\with_id.csv")
df2 = pd.read_csv(r'.fold1\f1_train - Copy.csv')
           
new = pd.merge(df1, df2, how="inner", on=["ID"])
new.to_csv(r".\f1_train_id.csv")
        
