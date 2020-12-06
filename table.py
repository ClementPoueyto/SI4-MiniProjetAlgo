import sys
import random
from generate_tree import generate_tree
from Main import algo

#genere le tableau des résultats
def generate_table():
    n=0
    p=0
    q=0
    graphs = generate_graphs(n,p,q)
    table = []
    for j in range (0,10):
        row = []
        for i in range(0,10):
            row.append(generate_cell(graphs))
        table.append(row)
    print(table)

#genere les n graphs en fonction des probabilités p et q
def generate_graphs(n,p,q):
    graphs =[]
    for i in range(0,n):
        graph = generate_tree(n,p,q)
        graphs.append(graph)
    return graphs

#genere une case en fonction des 100 graphes créés
def generate_cell(graphs):
    average = 0
    n=len(graphs)
    for i in range (0, n):
        res = algo(graphs[i][0],graphs[i][1])
        average=average+len(res)
        print(average)
    average=average/n
    return average
    


graphs = generate_graphs(10,0.4,0.5)
generate_cell(graphs)
