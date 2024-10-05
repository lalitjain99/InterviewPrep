#Since linked list is not a default data structure so we need to create a custom data structure using class
class Node:
    def __init__(self,data,next : None):

        self.data = data
        self.next = next

    
class LinkedList():

    def __init__(self):
        
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        else:
            new_node.next = self.head.next
            self.head = new_node

    def insertAtIndex(self,data,index):
        temp = Node(data)
        curr_node = self.head
        position = 0

        if index == 0:
            return self.insertAtBegin(data)
        
        while curr_node != None and position != index:
                position += 1
                curr_node = curr_node.next

        if curr_node != None:
            temp.next = curr_node.next
            curr_node.next = temp

        else:
            print("Index not found")

    def insertAtEnd(self,data):
        curr_node = self.head
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            return
        
        while curr_node != None:
            curr_node = curr_node.next

        curr_node.next = new_Node


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
            

