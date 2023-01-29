import numpy as np
import pandas as pd
import json
from scipy.stats import ttest_1samp

np.set_printoptions(suppress=True)

from sklearn.linear_model import LinearRegression
from sklearn import metrics

models = pd.read_pickle('bettermodel.pkl')

def expected(sex, age, precinct):
    # age <=> sex <=> precinct
    
    if sex is None:
        sex = .5
    elif sex == 'M':
        sex = 0.0
    else:
        sex = 1.0
        
    if age is None:
        age = 35.0
    
    if type(precinct)!= float or np.isnan(precinct):
        return .43
    
    precinct = str(int(precinct))
    mlr = models[precinct]

    return mlr.predict([[age, sex]])

with open("masterpiece.json") as file:
    masterpiece = json.load(file)
    
mailing = pd.read_pickle('mail.pkl')
canvassed = pd.read_pickle('walk.pkl')
called = pd.read_pickle('call.pkl')
texted = pd.read_pickle('text.pkl')

masterpiece = pd.DataFrame(masterpiece)

freq = np.zeros((7,3))
ex = np.zeros((7,3))
cost = np.zeros((7,3))

mapping = {'W': 0, 'C': 1, 'T': 2, 'M': 3}
cost_method = [2,  .13,    .06,    .35]
mail_freq = 0

# only keep these precincts
important = [9,10,11,44,46,285,347,379,411,430,431,664,752,792,793]

for ind, row in masterpiece.iterrows():
    meth = mapping[row['Method']]
    if meth != 3:
        cell = int(row['Day'])
        freq[cell][meth] += row['Voted']
        if (row['Precinct'] is not None) and row['Precinct'] in important:
            ex[cell][meth] += expected(row['Sex'], row['Age'], row['Precinct'])
    else:
        mail_freq += row['Voted']

counter_mail = 0

for index, row in mailing.iterrows():
    idm = mapping['M']
    counter_mail += cost_method[idm]
    
for index, row in canvassed.iterrows():
    day = row['Day']
    idm = mapping['W']
    cost[day][idm] += cost_method[idm]
    
for index, row in called.iterrows():
    day = row['Day']
    idm = mapping['C']
    cost[day][idm] += cost_method[idm]
    
for day in range(7):
    idm = mapping['W']
    print(cost[day][idm] / cost_method[idm])
    
for index, row in texted.iterrows():
    day = row['Day']
    idm = mapping['T']
    cost[day][idm] += cost_method[idm]
    

diff = freq - ex
metric = np.zeros((7,3))
sig_table = np.zeros((7,3))

for i in range(7):
     for j in range(3):
         metric[i][j] = round(cost[i][j]/diff[i][j], 2)
         stat, p = ttest_1samp(freq[i][j], ex[i][j])
         alpha = 0.01
         if p > alpha:
             sig_table[i][j] = False
         else:
             sig_table[i][j] = True

mail_metric = round((counter_mail)/(mail_freq - expected(row['Sex'], row['Age'], row['Precinct'])), 2)
stat, p = ttest_1samp(mail_freq, expected(row['Sex'], row['Age'], row['Precinct']))
alpha = 0.01
if p > alpha:
     sig = False
else:
     sig = True