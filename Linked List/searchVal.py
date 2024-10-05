class Node:

    def __init__(self,data,next_node = None):
        self.data = data 
        self.next = next_node

def searchValue(head,key):
    temp = head
    while temp != None:
        if temp.data == key:
            return True
        else:
            temp = temp.next 
    return False

arr = [1,2,3,4,5]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])
print("check if key is present in the linked list ",searchValue(head,31))