"""234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
 
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?"""
class Node:
    def __init__(self,data:int,next:None) -> None:
        self.data = data 
        self.next = next

#Approach 1: Iterative with extra space
#Time Complexity: O(2N)
#Space Complexity: O(N)
def isPalindrome(head):
    temp = head
    st = []
    while temp != None:
        st.append(temp.data)
        temp = temp.next

    temp = head

    while temp != None:
        if temp.data != st.pop():
            return False
        temp = temp.next 

    return True

#Approach 2: Using iteration and reverse with no extra space
#Time Complexity: 
#space Complexity:

def reverseLinkedList(head):
    if head is None or head.next is None:
        return head
    
    newHead = reverseLinkedList(head.next)
    front = head.next 
    front.next = head 
    head.next = None 
    return newHead

def isPalindrome(head):
    fast = head
    slow = head 

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next 

    newhead = reverseLinkedList(slow.next)

    first = head
    second = newhead

    while second:
        if first.data != second.data:
            reverseLinkedList(newhead)
            return False
        first = first.next 
        second = second.next 

    reverseLinkedList(newhead)

    return True

