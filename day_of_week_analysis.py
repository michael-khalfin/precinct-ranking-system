import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

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
    difference = np.subtract(contacted, reached)
    for ind in range(len(difference)):
        difference[ind] = 1.0/float(difference[ind])
    costs = np.multiply(money, difference)
    costs = [costs[ind] for ind in range(len(difference))]
    
    # normalize costs
    costs = [round(costs[ind]/sum(costs), 2) for ind in range(len(difference))]
    if r==0:
        plt.bar(['Mon', 'Tues', 'Wed', 'Thrs', 'Fri', 'Sat', 'Sun'], list(costs))
    elif r==1:
        i=len(costs)-1
        costs = np.array([sum(costs)-costs[i]-costs[i-1], costs[i-1], costs[i]])
        plt.bar(['Weekday', 'Sat', 'Sun'], list(costs))
    elif r==2:
        i=len(costs)-1
        costs = np.array([sum(costs)-costs[i]-costs[i-1], costs[i-1]+costs[i]])
        plt.bar(['Weekday', 'Weekend'], list(costs))
    return costs

if __name__ == "__main__":
    con = np.array([5.0,6.0,4.0,5.0,6.0,7.0,8.0])
    rea = np.array([1,1,2,2,1,4,5])
    money = np.array([10,12,14,15,9,8,4])
    
    fig = plt.figure(figsize=(10,5))
    relative_costs(con,rea,money)
    fig = plt.figure(figsize=(5,5))
    relative_costs(con,rea,money, r=1)
    fig = plt.figure(figsize=(4,5))
    relative_costs(con,rea,money, r=2)