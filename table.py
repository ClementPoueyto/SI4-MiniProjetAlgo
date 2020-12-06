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


# resultats : ( je fais gagner 20 min )
#[[100.0, 100.0, 99.98, 99.93, 99.58, 99.2, 98.48, 96.63, 91.59, 76.65],
#  [100.0, 100.0, 99.96, 99.93, 99.69, 99.23, 98.58, 97.14, 92.81, 75.35],
#  [100.0, 100.0, 99.99, 99.86, 99.59, 99.33, 98.25, 96.84, 91.92, 76.46],
# [100.0, 100.0, 99.99, 99.85, 99.74, 99.31, 98.45, 96.83, 92.26, 77.13],
#  [100.0, 100.0, 100.0, 99.9, 99.66, 99.23, 98.34, 96.6, 92.78, 78.17],
#  [100.0, 100.0, 99.99, 99.87, 99.65, 99.38, 98.39, 97.01, 92.24, 77.09],
#  [100.0, 100.0, 99.98, 99.88, 99.71, 99.35, 98.47, 96.12, 92.63, 76.84],
#  [100.0, 100.0, 99.96, 99.92, 99.7, 99.24, 98.38, 96.93, 92.12, 76.79],
#  [100.0, 100.0, 99.96, 99.9, 99.7, 99.23, 98.38, 96.34, 92.31, 78.12], 
# [100.0, 100.0, 100.0, 99.96, 99.77, 99.27, 98.55, 96.43, 92.29, 76.41]]