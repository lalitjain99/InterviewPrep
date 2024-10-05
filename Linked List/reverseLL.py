"""206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?"""





class Node:
    def __init__(self,data:int,next:None) -> None:
        self.data = data 
        self.next = None

#Approach 1: Iterative with extra memory
#Time Complexity: O(2N)
#Space Complexity: O(N)
def reverseLinkedList(head):
    temp = head
    st = []

    while temp != None:
        st.append(temp.data)
        temp = temp.next 

    temp = head
    while temp != None:
        temp.data = st.pop()
        temp = temp.next 

    return head


#Approach 2: Iterative with no extra memory
#Time Complexity: O(N)
#Space Complexity: O(1)

def reverseLinkedList(head):
    temp = head
    prev = None

    while temp != None:
        curr = temp.next 
        temp.next = prev
        prev = temp
        temp = curr

    return prev

#Approach 2: Recursion
#Time Complexity: O(N)
#Space Complexity: O(1)

def reverseLinkedList(head):

    if head is None or head.next is None:
        return head
    
    new_head = reverseLinkedList(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head