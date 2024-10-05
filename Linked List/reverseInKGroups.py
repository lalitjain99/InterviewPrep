"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple 
of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?"""
#Approach 1: Using reverse with recursion
#Time Complexity: O(N)
def reverse(head):
    if head is None or head.next is None:
        return head
    new_head = reverse(head.next)
    temp = head.next 
    temp.next = head 
    head.next = None
    return new_head

def findKNode(temp,k):
    k -= 1
    while temp != None and k>0:
        k -= 1
        temp = temp.next 
    return temp 

def reverseKGroup(head,K):
    temp = head 
    prevLast = None
    while temp:
        KNode = findKNode(temp,k)

        if KNode == None:
            if prevLast:
                prevLast.next = temp
                break
        next_node = KNode.next 
        KNode.next = None
        reverse(temp)
        if temp ==  head:
            head = KNode
        else:
            prevLast.next = KNode

        prevLast = temp
        temp = next_node

        return head