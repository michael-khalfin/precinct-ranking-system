import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

calls = pd.read_pickle('call.pkl')
walk = pd.read_pickle('walk.pkl')
text = pd.read_pickle('text.pkl')
mail = pd.read_pickle('mail.pkl')

# gender and age
male = 0
female = 0
age = {}
ranges = ['18-30', '30-40', '40-50','50-60','60+']

arr = [calls, walk, text, mail] 
for i in range(3):
    for ind, row in arr[i].iterrows():
        cell = row['Sex']
        if cell == 'F':
            female += 1
        elif cell == 'M':
            male += 1
        cell = row['Age']
        if 18 <= cell < 30:
            if '18-30' in age:
                age['18-30'] += 1
            else:
                age['18-30'] = 1
        elif 30 <= cell < 40:
            if '30-40' in age:
                age['30-40'] += 1
            else:
                age['30-40'] = 1
        elif 40 <= cell < 50:
            if '40-50' in age:
                age['40-50'] += 1
            else:
                age['40-50'] = 1
        elif 50 <= cell < 60:
            if '50-60' in age:
                age['50-60'] += 1
            else:
                age['50-60'] = 1
        else:
            if '60+' in age:
                age['60+'] += 1
            else:
                age['60+'] = 1
                
fig = plt.figure(figsize=(10,5))
plt.plot(ranges, [age[key] for key in ranges])
plt.xlabel('Age Range')
plt.ylabel('Frequency')