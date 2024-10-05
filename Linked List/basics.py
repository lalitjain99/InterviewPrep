# We have created a Node class in which we have defined a __init__ function to initialize the node with the data passed 
# as an argument and a reference with None because if we have only one node then there is nothing in its reference.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self,data,index):
        if index == 0:
            self.insertAtBegin(data)
        
        position = 0
        current_node = self.head

        while current_node != None and position != index:
            position += 1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

        else:
            print("Index not present")

    
    #inserting a node at end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    #update a node 
    def updateNode(self,val,index):
        position = 0
        curr_node = self.head

        if position == index:
            curr_node.data = val
        else:
            while curr_node != None and position != index:
                position += 1
                curr_node = curr_node.next

            if curr_node!= None:
                curr_node.data = val
            
            else:
                print("index not present")

    #delete a node
    def removeFirstNode(self):
        if self.head == None:
            return 
        
        self.head = self.head.next

    #remove last node
    def removeLastNode(self):
        if self.head == None:
            return
        curr_node = self.head
        while (curr_node.next != None and curr_node.next.next != None):
            curr_node = curr_node.next

        curr_node.next = None
