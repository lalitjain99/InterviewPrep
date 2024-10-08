"""138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in 
the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its 
value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point 
to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes 
x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of 
[val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point 
to any node.
Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""
#Approach 1: using intermediate Node (Not using extra space)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

def createCopyNode(head):
    temp = head
    while temp:
        copyNode = Node(temp.data)
        copyNode.next = temp.next
        temp.next = copyNode
        temp = copyNode.next

def connectRandomPointers(head):
    temp = head
    while temp:
        copyNode = temp.next 
        if temp.random:
            copyNode.random = temp.random.next
        else:
            copyNode.random = None
        temp = copyNode.next

def getDeepCopy(head):
    dummy = Node(-1)
    res = dummy
    temp = head
    while temp:
        res.next = temp.next 
        res = res.next

        temp.next = temp.next.next
        temp = temp.next

    return dummy.next


def createCopyNodes(head):
    if head is None:
        return head
    
    createCopyNode(head)
    connectRandomPointers(head)
    return getDeepCopy(head)

