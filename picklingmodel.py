import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

# with open('training_data.json') as file:
#     mapping = json.load(file)

bigframe = pd.read_pickle('dataframe.pkl')

important = ['9', '10','11','44','46','285','347', '379']
mapping = {}

bigframe = bigframe.fillna('0')

for precinct in important:
    df = bigframe[bigframe['Precinct'] == '0']
    mapping[precinct] = df

print(bigframe)

models = {}
lst = []

for precinct in mapping:
    # vars()[string(precinct)] = pd.DataFrame(mapping[precinct])
    df = mapping[precinct]
    
    df = df.dropna()
    
    for i, row in df.iterrows():
        val = 0.0
        if df.at[i, 'Sex'] == 'F':
            val = 1.0
        df.at[i,'Sex'] = val
        df.at[i, 'Age'] = float(df.at[i, 'Age'])
        df.at[i, 'Voted'] = float(int(df.at[i, 'Voted']))

    df_train = df.sample(frac = 0.68)
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
    rsq = mlr.score(x_test,y_test)*100
    lst.append(rsq)
    print('R squared: {:.2f}'.format(rsq))
    print('Mean Absolute Error:', meanAbErr)
    print('Mean Square Error:', meanSqErr)
    print('Root Mean Square Error:', rootMeanSqErr)

    models[precinct] = mlr

print(lst)
print(50*'-')
print(sum(lst)/len(lst))
print(50*'-')


for precinct in models:
    print(models[precinct].predict([[20.0, 1.0]]))

filehandler = open('models.pkl', 'wb') 
pickle.dump(models, filehandler)

