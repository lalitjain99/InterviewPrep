class Node():

    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def lengthLL(head):
    cnt = 0
    temp = head 

    while temp != None:
        temp = temp.next 
        cnt += 1

    return cnt

arr = [1,2,3,4,5]
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])
print("length of linked list is ",lengthLL(head))

