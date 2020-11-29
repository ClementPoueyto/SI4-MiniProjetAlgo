import sys
from generate_tree import generate_tree

def findMax(edges,vertices):
    assoc = {}
    for elm in edges.keys():
        if edges[elm] == "B" and vertices[elm[0]] == "R" and vertices[elm[1]] == "R":
            assoc[elm[1]] = 1 if elm[1] not in assoc else assoc[elm[1]] + 1
            assoc[elm[0]] = -1 if elm[0] not in assoc else assoc[elm[0]] - 1   
    if not assoc:
        assoc = list(filter(lambda x: vertices[x]=="R", vertices.keys()))
        return assoc[0]
    return max(assoc.keys(),key=lambda x:assoc[x])

def main():
    vertices,edges = generate_tree(5,0.2,0.4)
    
    #### Parser d'entrée ####
    # V,E = map(int,input().split())
    # for _ in range(V):
    #     n,c = map(str,input().split())
    #     vertices[n]= c
    # for _ in range(E):
    #     v1,v2,c = map(str,input().split())
    #     edges[(v1,v2)] = c

    order = []
    while len(list(filter(lambda x:vertices[x]=="R",vertices.keys())))>0:
        v = findMax(edges,vertices);
        order.append(v)
        del vertices[v]
        keys = list(edges.keys())
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
    print(order)

main()
