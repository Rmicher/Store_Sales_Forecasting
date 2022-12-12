# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:57:30 2022

@author: rober
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


os.listdir("C:/Users/rober/OneDrive/Documents/Data Projects/Store Sales Time Series Forecasting")

#Wages in the public sector are paid every two weeks on the 15 th and on 
#the last day of the month. Supermarket sales could be affected by this.

#A magnitude 7.8 earthquake struck Ecuador on April 16, 2016. 
#People rallied in relief efforts donating water and other first need products 
#which greatly affected supermarket sales for several weeks after the earthquake.



oil_data = pd.read_csv("oil.csv", parse_dates=['date'], index_col='date') #forward fill, backwards fill
oil_data['dcoilwtico'].fillna(method="bfill", limit=2, inplace=True)

holiday_data = pd.read_csv("holidays_events.csv", parse_dates=['date'], index_col='date')
trans_data = pd.read_csv("transactions.csv", parse_dates=['date'], index_col='date')


stores_data = pd.read_csv("stores.csv")



train_data = pd.read_csv("train.csv", parse_dates=['date'], index_col='date')
test_data = pd.read_csv("test.csv", parse_dates=['date'], index_col='date')
sample_submission = pd.read_csv("sample_submission.csv")


###### 


trans_data.plot()

agg_data = trans_data.groupby([trans_data.index.year, trans_data.index.month])['transactions'].sum()

agg_data.plot()
