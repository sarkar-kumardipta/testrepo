# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:57:24 2021

@author: kumar
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

df = pd.read_csv("C:\KDS\IBM data science\data\Car data\data.csv")
print(df.head(5))

print(df.tail(5))

print(df.dtypes)

df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
print(df.head(5))

df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
print(df.head(5))

print(df.shape)

duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

print(df.count())