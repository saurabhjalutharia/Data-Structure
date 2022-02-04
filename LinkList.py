import os
os.system("cls")

class Node():
    def __init__(self,data):
        self.data = data
        self.nodeLink = None

class LinkList():
    def __init__(self):
        self.head = None
        self.size = 0
    #----------------------------------------------------------------------------------------------------------------
    def insertBegin(self,data):
        newNode = Node(data)
        self.size += 1
        if self.head == None:
            self.head = newNode
        else:
            newNode.nodeLink = self.head
            self.head = newNode
    #----------------------------------------------------------------------------------------------------------------
    def insertLast(self,data):
        newNode = Node(data)
        self.size += 1
        currentNode = self.head
        if self.head == None:
            self.head = newNode
        else:
            while currentNode.nodeLink is not None:
                currentNode = currentNode.nodeLink
            currentNode.nodeLink = newNode
    #----------------------------------------------------------------------------------------------------------------
    def insertAfterData(self,afterdata,data):
        currentNode = self.head
        newNode = Node(data)
        if self.head == None:
            if currentNode.data == afterdata:
                newNode.nodeLink = currentNode.nodeLink
                currentNode.nodeLink = newNode
                self.size += 1
            else:
                print("After_Node data does not exists.")
        else:
            while currentNode.nodeLink is not None:
                if currentNode.data == afterdata:
                    newNode.nodeLink = currentNode.nodeLink
                    currentNode.nodeLink = newNode
                    self.size += 1
                    break
                else:
                    currentNode = currentNode.nodeLink
            if currentNode.nodeLink == None:
                print("After_Node data does not exists.")
    
    #----------------------------------------------------------------------------------------------------------------
    def insertBeforeData(self,beforedata,data):
        currentNode = self.head
        newNode = Node(data)
        if self.head == None:
            if currentNode.data == beforedata:
                newNode.nodeLink = currentNode
                currentNode.nodeLink = newNode
                self.size += 1
            else:
                print("Before_Node Data does not exists.")
        else:
            while currentNode.nodeLink is not None:
                if currentNode.nodeLink.data == beforedata:
                    newNode.nodeLink = currentNode.nodeLink
                    currentNode.nodeLink = newNode
                    self.size += 1
                    break
                else:
                    currentNode = currentNode.nodeLink
            if currentNode.nodeLink == None:
                print("Before_Node Data does not exists.")
    #----------------------------------------------------------------------------------------------------------------
    def insertAfterIndex(self,afterindex,data):
        countIndex = 1
        currentNode = self.head
        newNode = Node(data)
        if self.head == None:
            self.insertLast(data)
            countIndex += 1
        else:
            while currentNode is not None:
                if countIndex == afterindex:
                    newNode.nodeLink = currentNode.nodeLink
                    currentNode.nodeLink = newNode
                    break
                else:
                    countIndex += 1
                    currentNode = currentNode.nodeLink
            if currentNode == None:
                print("Node Index does not exists.")

    #----------------------------------------------------------------------------------------------------------------
    def insertBeforeIndex(self,beforeindex,data):
        countIndex = 1
        currentNode = self.head
        previousNode = None
        newNode = Node(data)
        if self.head == None:
            self.insertBegin(data)
            countIndex += 1
        elif countIndex == beforeindex:
            self.insertBegin(data)
            countIndex += 1
        else:
            while currentNode is not None:
                if countIndex == beforeindex:
                    newNode.nodeLink = previousNode.nodeLink
                    previousNode.nodeLink = newNode
                    break
                else:
                    countIndex += 1
                    previousNode = currentNode
                    currentNode = currentNode.nodeLink       
            if currentNode == None:
                print("Node Index does not exists.")
    #----------------------------------------------------------------------------------------------------------------
    def traverse(self):
        currentNode = self.head
        if self.head == None:
            print(f"{self.head.data}")
        else:
            while currentNode.nodeLink is not None:
                print(f"{currentNode.data} -> ", end = "")
                currentNode = currentNode.nodeLink
            print(f"{currentNode.data}")
    #----------------------------------------------------------------------------------------------------------------
    def linkSize(self):
        return self.size

#----------------------------------------------------------------------------------------------------------------
linkListObject = LinkList()
#----------------------------------------------------------------------------------------------------------------
linkListObject.insertBegin(10)
linkListObject.insertBegin(8)
linkListObject.insertBegin(6)
linkListObject.insertBegin(4)
linkListObject.insertBegin(2)
#----------------------------------------------------------------------------------------------------------------
linkListObject.insertLast(12)
linkListObject.insertLast(18)
linkListObject.insertLast(20)
#----------------------------------------------------------------------------------------------------------------
linkListObject.insertAfterData(12, 14)
# #----------------------------------------------------------------------------------------------------------------
linkListObject.insertBeforeData(18, 16)
# #----------------------------------------------------------------------------------------------------------------
linkListObject.insertAfterIndex(10, 22)
linkListObject.insertLast(24)
linkListObject.insertLast(26)
linkListObject.insertLast(28)
#----------------------------------------------------------------------------------------------------------------
linkListObject.insertBeforeIndex(1, 0)
linkListObject.insertAfterIndex(1, 1)
#----------------------------------------------------------------------------------------------------------------
linkListObject.traverse()
#----------------------------------------------------------------------------------------------------------------
print("Size of Link List is : - ", linkListObject.linkSize())
print("")
#----------------------------------------------------------------------------------------------------------------
