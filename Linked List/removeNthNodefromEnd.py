"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

#Approach 1: Brute 
#Time Complexity :-> O(L) + O(L-N) --> O(2L)
#space Complexity :-> O(1)
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None

def removeNthFromEnd(head,n):
    temp = head
    cnt = 0
    while temp:
        cnt +=1 
        temp = temp.next 

    if cnt == n:
        new_head = head.next
        return new_head
    
    res = cnt-n
    temp = head

    while temp:
        res -= 1

        if res == 0:
            break

        temp = temp.next 

    delete_node = temp.next 

    temp.next = temp.next.next 

    return head

#Approach 2: Two pointers for single traversal
#Time Complexity :-> O(L) 
#space Complexity :-> O(1)

def removeNthFromEnd(head,n):
    fastptr = head
    
    for i in range(n):
        fastptr = fastptr.next 

    #base condition
    #only single node is present 
    if fastptr == None:
        return head.next
    
    slwptr = head
    #fastptr need to be stopped at last node so we need to check fastptr.next is not none for traversing
    while fastptr.next != None:
        slwptr = slwptr.next 
        fastptr = fastptr.next 

    slwptr.next = slwptr.next.next 

    return head

    

