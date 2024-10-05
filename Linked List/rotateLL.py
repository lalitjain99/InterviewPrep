"""61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500]. 
-100 <= Node.val <= 100
0 <= k <= 2 * 109"""
#Approach 1:
#Time Complexity: O(N+N)
#Space Complexity: O(1)

def rotateLL(head,k):
    if head == None or head.next == None or k == 0:
        return head
    
    tail = head
    length = 1
    while tail.next:
        length +=1
        tail = tail.next
    
    if k == length:
        return head
    
    tail.next = head
    k = k%length
    end =length - k
    while end:
        tail = tail.next
        end -= 1

    head =tail.next
    tail.next = None 

    return head


