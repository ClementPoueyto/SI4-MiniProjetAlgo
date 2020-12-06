import sys
import random
from generate_tree import generate_tree
from Main import algo

#genere le tableau des résultats
#n : nb sommet pour un graphe
#nbCol : nombre de colonnes dans le tableau
#nbRow : nombre de lignes dans le tableau

def generate_table(n=100,nbCol=10, nbRow=10):
    incrValueCol = 1/nbCol
    incrValueRow= 1/nbRow
    p=0.1
    q=0
    graphs = []
    table = []
    for j in range (0,nbRow):
        row = []
        q=0
        for i in range(0,nbCol):
            graphs = generate_graphs(n,p,q)
            row.append(generate_cell(graphs))
            q=round(q+incrValueCol, 2)
        table.append(row)
        p=round(p+incrValueRow, 2)

    return table

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
    average=round(float(average/n), 2)
    return average
    

print(generate_table())
