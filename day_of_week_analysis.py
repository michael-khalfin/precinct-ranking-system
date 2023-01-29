import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import set_matplotlib_formats

set_matplotlib_formats('retina', quality=100)
plt.rcParams['figure.figsize'] = (8, 5)

def relative_costs(contacted, reached, money, day=0, r=0):
    """
    

    Parameters
    ----------
    1xn matrices
    contacted : The number of people that were contacted (Size of the data frame).
    reached : The number of people that were reached (Partition of the data frame).
    money : The amount of money spent to contact people.
    
    ints
    day : The day of the week (0 - Mon, 1 - Tues, ..., 7 - Sun)
    r : Representation of the data (0 - Mon, Tues, ..., Sun
                                    1 - Weekday, Sat, Sun
                                    2 - Weekday, Weekend)

    Returns
    -------
    costs : A vector representation of the costs/vote, normalized to [0,1].

    """
    
    # calculate the costs/vote

    difference = reached
    for ind in range(len(difference)):
        difference[ind] = 1.0/float(difference[ind])
    costs = np.multiply(money, difference)
    costs = [costs[ind] for ind in range(len(difference))]
    
    # we could normalize costs

    if r==0:
        plt.bar(['Mon', 'Tues', 'Wed', 'Thrs', 'Fri', 'Sat', 'Sun'], list(costs))
        plt.ylabel('Efficiency ($/Vote)')
    elif r==1:
        i=len(costs)-1
        costs = np.array([sum(costs)-costs[i]-costs[i-1], costs[i-1], costs[i]])
        plt.style.use('seaborn-deep')
        plt.bar(['Weekday', 'Saturday', 'Sunday'], list(costs), color='darkgreen')
        plt.xlabel('Day of Week')
        plt.ylabel('$/Successful Contact')
        plt.title('Efficiency of Reaching a Contact')
        plt.show()
        
    elif r==2:
        i=len(costs)-1
        costs = np.array([sum(costs)-costs[i]-costs[i-1], costs[i-1]+costs[i]])
        fig, ax = plt.subplots()
        
        bars = ax.bar(
            x=['Weekday', 'Weekend'],
            height=list(costs)
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

        ax.set_ylabel('Efficiency ($/Vote)', labelpad=15, color='#333333')
        ax.set_title('Efficiency of Spending Per Day of Week', pad=15, color='#333333',
             weight='bold')
        
        fig.tight_layout()
        
    return costs

def make_array(df, contacted, cost = 1):
    """
    

    Parameters
    ----------
    df : Any arbitrary data frame.
    contacted: True/ False

    Returns
    -------
    arr : 1xn numpy array (frequency matrix) where each entry is a day of the week.

    """
    arr = np.zeros(7)
    for ind, row in df.iterrows():
        arr[row['Day']] += int(contacted or row['Reached']) * cost
    return arr
    
if __name__ == "__main__":
    calls = pd.read_pickle('call.pkl')
    mail = pd.read_pickle('mail.pkl')
    walk = pd.read_pickle('walk.pkl')
    text = pd.read_pickle('text.pkl')
    
    contacted = make_array(calls, True) + make_array(mail, True) + make_array(walk, True) + make_array(text, True)
    reached = make_array(calls, False) + make_array(mail, False) + make_array(walk, False) + make_array(text, False)
    cost = make_array(calls, True, .06) + make_array(mail, True, .35) + make_array(walk, True, 2) + make_array(text, True, .13)
    
    relative_costs(contacted, reached, cost, r=1)