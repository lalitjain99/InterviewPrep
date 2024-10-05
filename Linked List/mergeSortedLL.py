"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""
class Node:
    def __init__(self,data:int,next:None) -> None:
        self.data = data 
        self.next = None
def mergeSortedLL(list1,list2):
    t1 = list1
    t2 = list2 
    dummy = Node(-1)
    temp = dummy 

    while t1 and t2:
        if t1.data < t2.data:
            temp.next = t1
            temp = t1
            t1 = t1.next 
        else:
            temp.next = t2
            temp = t2
            t2 = t2.next

    if t1:
        temp.next = t1
    if t2:
        temp.next = t2

    return dummy.next