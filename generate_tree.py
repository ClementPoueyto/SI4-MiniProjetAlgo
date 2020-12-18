import sys
import random

#n : nombre de sommets
#p : probabilité pour sommet etre rouge
#q : probabilité pour arc etre bleu
def generate_tree_old(n, p, q):
    nE = n*(n - 1)
    eB = ['B' for _ in range(int(nE * q))]
    eR = ['R' for _ in range(nE - int(nE * q))]
    e = eR + eB
    random.shuffle(e)
    vR = ['R' for _ in range(int(n * p))]
    vB = ['B' for _ in range(n - int(n * p))]
    v = vR + vB
    random.shuffle(v)
    vertices = {}
    edges = {}
    i = 0
    for j in range(len(v)):
        vertices[j] = v[j]
        for k in range(j):
            edges[k,j] = e[i]
            edges[j,k] = e[i+1]
            i+=2
    return vertices, edges

def generate_tree(n, p, q):
    nE = n*(n - 1)
    vertices = {}
    edges = {}
    for i in range(n):
        vertices[i] = "R" if random.randint(0,100) < p*100 else "B"
        for j in range(i):
            edges[i,j] = "B" if random.randint(0,100) <= q*100 else "R"
            edges[j,i] = "B" if random.randint(0,100) <= q*100 else "R"
    return vertices, edges
