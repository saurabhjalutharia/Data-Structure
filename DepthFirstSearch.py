import os
from re import I
os.system('cls')
#-------------------------------------------------------------------------------------------------
class Node():
    def __init__(self,data):
        self.data = data
        self.adjancetList = []
        self.visited = False
#-------------------------------------------------------------------------------------------------
class DFS():
    def dfsTraaverse(self,node):
        node.visited = True
        print(f"{node.data} -> ", end='')
        for i in node.adjancetList:
            if not i.visited:
                self.dfsTraaverse(i)
#-------------------------------------------------------------------------------------------------
A = Node("A")               #                            A
B = Node("B")               #                          /   \
C = Node("C")               #                         B     E
D = Node("D")               #                       /   \   |
E = Node("E")               #                     C      D  Z   
F = Node("F")               #                    /      / \
G = Node("G")               #                   F      G   H
H = Node("H")               #                          |   |
I = Node("I")               #                          L   I
J = Node("J")               #                             / \
K = Node("K")               #                            J   K  
Z = Node("Z")                   
L = Node("L")                  
#-------------------------------------------------------------------------------------------------
A.adjancetList.append(B)
A.adjancetList.append(E)
B.adjancetList.append(C)
B.adjancetList.append(D)
C.adjancetList.append(F)
D.adjancetList.append(G)
D.adjancetList.append(H)
G.adjancetList.append(L)
H.adjancetList.append(I)
I.adjancetList.append(J)
I.adjancetList.append(K)
E.adjancetList.append(Z)
#-------------------------------------------------------------------------------------------------
dfsTraverseStart = A
dfsObject = DFS()
dfsObject.dfsTraaverse(dfsTraverseStart)
print("\n")
#-------------------------------------------------------------------------------------------------


