class Node:
    def __init__(self,data,next:None):
        self.data = data
        self.next = next


def convertArrayLL(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head
    