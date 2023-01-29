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
ages = [0] * 20

arr = [calls, walk, text, mail] 
for i in range(3):
    for ind, row in arr[i].iterrows():
        cell = row['Sex']
        if cell == 'F':
            female += 1
        elif cell == 'M':
            male += 1
        try:
            cell = int(row['Age'])
            ages[cell//5] += 1
        except:
            pass

fig = plt.figure(figsize=(15,5))
plt.bar(['{}-{}'.format(i*5, i*5+4) for i in range(20)], ages)
plt.xlabel('Age Range')
plt.ylabel('Frequency')