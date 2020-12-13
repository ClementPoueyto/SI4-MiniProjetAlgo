import sys
import random
from generate_tree import generate_tree
from Main import algo
import time
import xlsxwriter

#genere le tableau des résultats
#n : nb sommet pour un graphe
#nbCol : nombre de colonnes dans le tableau
#nbRow : nombre de lignes dans le tableau

def generate_table(n=100,nbCol=10, nbRow=10):
    incrValueCol = 1/nbCol
    incrValueRow= 1/nbRow
    p=0
    q=0
    graphs = []
    table = []
    for j in range (0,nbRow+1):
        row = []
        q=0
        print(str(j*nbRow)+'%'+" achieved")
        for i in range(0,nbCol+1):
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

def fromArrayToExcel(array):
    workbook = xlsxwriter.Workbook('arrays.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    for col, data in enumerate(array):
        worksheet.write_row(col, row, data)

    workbook.close()
        
t1 = time.time()
res=generate_table()

print(res)
fromArrayToExcel(res)
#print(generate_table())
t2 = time.time()
print(t2-t1)
# resultats : ( je fais gagner 20 min )
#[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
#  [100.0, 99.99, 99.93, 99.91, 99.58, 99.29, 98.45, 96.92, 92.09, 77.34, 1.0], 
# [100.0, 99.98, 99.93, 99.89, 99.56, 99.2, 97.98, 96.82, 92.16, 76.78, 1.0], 
# [100.0, 99.98, 99.92, 99.83, 99.53, 99.29, 98.38, 96.59, 92.53, 76.76, 1.0], 
# [100.0, 100.0, 99.92, 99.86, 99.66, 99.27, 98.35, 96.39, 92.04, 76.16, 1.0], 
# [100.0, 100.0, 99.96, 99.86, 99.69, 99.28, 98.41, 96.43, 91.87, 74.9, 1.0],
#  [100.0, 100.0, 99.91, 99.88, 99.46, 99.2, 98.28, 96.32, 91.48, 75.61, 1.0], 
# [100.0, 99.99, 99.92, 99.83, 99.7, 99.06, 97.92, 96.48, 91.85, 76.37, 1.0],
#  [100.0, 99.98, 99.95, 99.84, 99.58, 99.19, 98.48, 97.07, 92.31, 75.7, 1.0], 
# [100.0, 99.98, 99.93, 99.88, 99.55, 99.18, 98.25, 96.28, 92.05, 75.72, 1.0], 
# [100.0, 100.0, 99.92, 99.83, 99.55, 99.21, 98.43, 96.28, 92.23, 75.77, 1.0]]