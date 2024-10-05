"""
Given a linked list where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list 
such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the middle of 0s and 2s.

Examples:

Input: LinkedList: 1->2->2->1->2->0->2->2
Output: 0->1->1->2->2->2->2->2
Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.
 
Input: LinkedList: 2->2->0->1
Output: 0->1->2->2
Explanation: After arranging all the 0s,1s and 2s in the given format, the output will be 0 1 2 2.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= no. of nodes <= 106
0 <= node->data <= 2
"""
class Node:
    def __init__(self,data) -> None:
         self.data = data 
         self.next = None

def segregate(self, head):
        #code here
        dummyhead0 = Node(-1)
        zero = dummyhead0
        dummyhead1 = Node(-1)
        one = dummyhead1
        dummyhead2 = Node(-1)
        two = dummyhead2
        
        temp = head
        
        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = zero.next
                
            elif temp.data == 1:
                one.next = temp
                one = one.next
              
            else:
                two.next = temp
                two = two.next
            temp = temp.next

        if dummyhead1.next:
            zero.next = dummyhead1.next
        else:
            zero.next = dummyhead2.next
            
        one.next = dummyhead2.next
        new_head = dummyhead0.next
        two.next = None
        return new_head