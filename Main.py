import sys
from generate_tree import generate_tree
import time

def findMax(edges,vertices):
    assoc = {}
    for elm in edges.keys():
        if edges[elm] == "B" and vertices[elm[0]] == "R" and vertices[elm[1]] == "R":
            assoc[elm[1]] = 1 if elm[1] not in assoc else assoc[elm[1]] + 1
            assoc[elm[0]] = -1 if elm[0] not in assoc else assoc[elm[0]] - 1
        elif edges[elm] == "R" and vertices[elm[0]] == "R" and vertices[elm[1]] == "B":
            assoc[elm[0]] = 1 if elm[0] not in assoc else assoc[elm[0]] + 1
        elif edges[elm] == "R" and vertices[elm[0]] == "R" and vertices[elm[1]] == "R":
            assoc[elm[1]] = -1 if elm[1] not in assoc else assoc[elm[1]] - 1
        else:   
            if not assoc and vertices[elm[0]] == 'R':
                assoc[elm[0]] = 0
            if not assoc and vertices[elm[1]] == 'R':
                assoc[elm[1]] = 0
    if not assoc:
        return list(vertices.keys())[list(vertices.values()).index("R")]
    return max(assoc.keys(),key=lambda x:assoc[x])

def algo(vertices, edges):    
    order = []
    while len(list(filter(lambda x:vertices[x]=="R",vertices.keys())))>0:
        
        v = findMax(edges,vertices)
        order.append(v)
        del vertices[v]
        keys = list(filter(lambda x: x[0]==v or x[1]==v,edges.keys()))
        i = 0 
        while i<len(keys):
            if keys[i][0]==v:
                if edges[keys[i]] == "R":
                    vertices[keys[i][1]] = "R"
                else :
                    vertices[keys[i][1]] = "B"
                del edges[keys[i]]
            if keys[i][1]==v:
                del edges[keys[i]]
            i+=1
    return order

def main():
    vertices,edges = generate_tree(1000,1,0)
    #### Parser d'entrée ####
    # V,E = map(int,input().split())
    # for _ in range(V):
    #     n,c = map(str,input().split())
    #     vertices[n]= c
    # for _ in range(E):
    #     v1,v2,c = map(str,input().split())
    #     edges[(v1,v2)] = c
    algo(vertices,edges)
    # print(algo(vertices,edges))


# t1 = time.time()
#main()
# t2 = time.time()
# print(t2-t1)
