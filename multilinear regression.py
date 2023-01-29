# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 17:51:25 2023

@author: Marko
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# load dataset
df = pd.read_pickle('dataframe.pkl')

df = df.dropna()
df = df.drop('Method', axis = 1)
df = df.drop('Reached', axis = 1)
df = df.drop('Day', axis = 1)
df = df.drop('Zip', axis = 1)
df = df.drop('Precinct', axis = 1)


for i, row in df.iterrows():
    val = 0.0
    if df.at[i, 'Sex'] == 'F':
        val = 1.0
    df.at[i,'Sex'] = val
    df.at[i, 'Age'] = float(df.at[i, 'Age'])
    df.at[i, 'Voted'] = float(int(df.at[i, 'Voted']))

df_train = df.sample(frac = 0.7)
df_test = df.drop(df_train.index)

x_train = df_train[['Age', 'Sex']]
x_test = df_test[['Age', 'Sex']]
y_train = df_train['Voted']
y_test = df_test['Voted']


mlr = LinearRegression()  
mlr.fit(x_train, y_train)

print("Intercept: ", mlr.intercept_)
print("Coefficients:")
list(zip(x_train, mlr.coef_))

y_pred_mlr= mlr.predict(x_test)
print("Prediction for test set: {}".format(y_pred_mlr))

mlr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_mlr})

meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
print('R squared: {:.2f}'.format(mlr.score(x_test,y_test)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)

print(mlr.predict([[68.0, 1.0]]))



