"""You are given a linked list where each element in the list is a node and have an integer data. 
You need to add 1 to the number formed by concatinating all the list node numbers together and return the head of the modified linked list. 

Note: The head represents the first element of the given array.

Examples :

Input: LinkedList: 4->5->6
Output: 457

Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 
Input: LinkedList: 1->2->3
Output: 124
 
Explanation:  1->2->3 represents 123 and when 1 is added it becomes 124. 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= len(list) <= 105
0 <= list[i] <= 9 """

class Node:
    def __init__(self,data:int,next:None) -> None:
        self.data = data 
        self.next = None

#Approach 1: Iterative using reverse
#Time Complexity:O(3N)
#Space Complexity:O(1)

def reverse(head):
    if head is None or head.next is None:
        return head 
    newhead = reverse(head.next)
    front = head.next 
    front.next = head 
    head.next = None
    return newhead

def addOne(head):
    head = reverse(head)
    temp = head
    carry = 1
    while temp != None:
        sum = temp.data + carry
        digit = sum%10
        carry = sum//10
        temp.data = digit
        if carry == 0:
            break
        temp = temp.next 

    if carry == 1:
        new_head = reverse(head)
        new_node = Node(1)
        new_node.next = head
        return new_node
    
    head = reverse(head)
    return head

#Approach 2: using recursion
#Time Complexity:O(3N)
#Space Complexity:O(1)

def recursive(self,temp):
        if temp is None:
            return 1
        
        carry = self.recursive(temp.next)
        temp.data = temp.data + carry
        if temp.data<10:
            return 0
        temp.data = 0
        return 1
    
def addOne(self,head):
    carry =  self.recursive(head)
    if carry ==1:
        new_node = Node(1)
        new_node.next = head
        return new_node
        
    return head
    
    