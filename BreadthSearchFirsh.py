import os
os.system("cls")
#-------------------------------------------------------------------------------------------------
class Node():
    def __init__(self,data):
        self.data = data
        self.visited = False
        self.adjacentNodeList = []
#-------------------------------------------------------------------------------------------------
class BFS():
    def bfsSearch(self, node):
        bfsqueeue = []
        node.visited = True
        bfsqueeue.append(node)
        while bfsqueeue:
            currentNode = bfsqueeue.pop(0)
            print(f"{currentNode.data} -> ",end="")
            for i in currentNode.adjacentNodeList:
                if not i.visited:
                    i.visited = True
                    bfsqueeue.append(i)        
#-------------------------------------------------------------------------------------------------
A = Node("A")               #                            A
B = Node("B")               #                          /   \
C = Node("C")               #                        B       E
D = Node("D")               #                       /   \    |
E = Node("E")               #                     C      D   Z   
F = Node("F")               #                    /      / \
G = Node("G")               #                   F      G   H
H = Node("H")               #                          |   |
I = Node("I")               #                          L   I
J = Node("J")               #                             / \
K = Node("K")               #                            J   K  
Z = Node("Z")                   
L = Node("L")                                   
#-------------------------------------------------------------------------------------------------
A.adjacentNodeList.append(B)
A.adjacentNodeList.append(E)
B.adjacentNodeList.append(C)
B.adjacentNodeList.append(D)
C.adjacentNodeList.append(F)
D.adjacentNodeList.append(G)
D.adjacentNodeList.append(H)
G.adjacentNodeList.append(L)
H.adjacentNodeList.append(I)
I.adjacentNodeList.append(J)
I.adjacentNodeList.append(K)
E.adjacentNodeList.append(Z)
#-------------------------------------------------------------------------------------------------
startNode = A
bfsObject = BFS()
bfsObject.bfsSearch(startNode)
print("\n")
#-------------------------------------------------------------------------------------------------
