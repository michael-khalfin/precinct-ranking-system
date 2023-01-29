import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

set_matplotlib_formats('retina', quality=100)
plt.rcParams['figure.figsize'] = (8, 5)

calls = pd.read_pickle('call.pkl')
walk = pd.read_pickle('walk.pkl')
text = pd.read_pickle('text.pkl')
mail = pd.read_pickle('mail.pkl')

# gender and age
male = 0
female = 0
ages = [0] * 20

arr = [calls, walk, text, mail] 
for i in range(4):
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

plt.style.use('seaborn-talk')
fig, ax = plt.subplots()

# fig = plt.figure(figsize=(15,5))
# plt.bar(['{}-{}'.format(i*5, i*5+4) for i in range(20)], ages)
# plt.xlabel('Age Range')
# plt.ylabel('Frequency')

bars = ax.bar(
    x = ['{}-{}'.format(i*5, i*5+4) for i in range(3,20)],
    height = ages[3:20]
)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

bar_color = bars[0].get_facecolor()
for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        round(bar.get_height(), 1),
        horizontalalignment='center',
        color=bar_color,
        weight='bold'
        )

ax.set_xlabel('Age Range', labelpad=15, color='#333333')
ax.set_ylabel('Frequency', labelpad=15, color='#333333')
ax.set_title('Frequency Bar Chart of People Who Voted', pad=15, color='#333333',
     weight='bold')

fig.tight_layout()