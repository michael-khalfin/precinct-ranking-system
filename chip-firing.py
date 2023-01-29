import networkx as nx
from gurobipy import *

def create_graph():
    G = nx.complete_graph(8)
    return G

def visualize_network(G):
    """ visualizes network
    """
    pos = nx.circular_layout(G)
    nx.draw(G, pos, node_size = 10, width = 0.4, arrowsize = 2)

def chip_firing(precincts, totals, partials):
    #bound = min([precinct[1] for precinct in precincts.keys()])
    #bound //= 2
    #optimal = 0
    #for i in range(bound):
    #    for precinct in precincts.keys():
    #        precinct[1] -= 1
    m = Model()
    x1 = m.addVar(vtype=GRB.INTEGER, name='x1')
    x2 = m.addVar(vtype=GRB.INTEGER, name='x2')
    x3 = m.addVar(vtype=GRB.INTEGER, name='x3')    
    x4 = m.addVar(vtype=GRB.INTEGER, name='x4')
    x5 = m.addVar(vtype=GRB.INTEGER, name='x5')
    x6 = m.addVar(vtype=GRB.INTEGER, name='x6')
    x7 = m.addVar(vtype=GRB.INTEGER, name='x7')
    x8 = m.addVar(vtype=GRB.INTEGER, name='x8')
    
    MIN = .30
    MAX = .55
    
    m.setObjective(x1/totals[0]+x2/totals[1]+x3/totals[2]+x4/totals[3]+
                   x5/totals[4]+x6/totals[5]+x7/totals[6]+x8/totals[7])
    m.addConstr(x1+x2+x3+x4+x5+x6+x7+x8==sum(partials))
    m.addConstr(x1/totals[0] <= MAX)
    m.addConstr(x1/totals[0] >= MIN)
    m.addConstr(x2/totals[1] <= MAX)
    m.addConstr(x2/totals[1] >= MIN)
    m.addConstr(x3/totals[2] <= MAX)
    m.addConstr(x3/totals[2] >= MIN)
    m.addConstr(x4/totals[3] <= MAX)
    m.addConstr(x4/totals[3] >= MIN)
    m.addConstr(x5/totals[4] <= MAX)
    m.addConstr(x5/totals[4] >= MIN)
    m.addConstr(x6/totals[5] <= MAX)
    m.addConstr(x6/totals[5] >= MIN)
    m.addConstr(x7/totals[6] <= MAX)
    m.addConstr(x7/totals[6] >= MIN)
    m.addConstr(x8/totals[7] <= MAX)
    m.addConstr(x8/totals[7] >= MIN)
    
    m.optimize()
    new_partials = []
    for v in m.getVars():
        new_partials.append(v.x)
        #print(v.varName, v.x)
    
    change = []
    i = 0
    while i <= 7:
        change.append(new_partials[i] - partials[i])
        i += 1
    return new_partials, change

if __name__ == '__main__':
    G = create_graph()
    visualize_network(G)
    # organized by precinct : total, turnout
    precincts = [9, 10, 11, 44, 46, 285, 347, 379]
    totals = [2625, 1974, 1903, 2222, 2760, 2889, 3931, 2127]
    partials = [1109, 685, 659, 892, 879, 931, 1527, 804]
    results = chip_firing(precincts, totals, partials)
    old_percents = [partials[i] / totals[i] for i in range(8)]
    new_percents = [results[0][i] / totals[i] for i in range(8)]