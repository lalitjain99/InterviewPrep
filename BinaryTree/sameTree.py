"""100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 
Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104"""
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None 


def sameTree(p:TreeNode,q:TreeNode):
    #if both trees are empty
    if not p and not q:
        return True 
    #if either p or q is none or values doesn't match 
    if not p or not q or p.val != q.val:
        return False
    else:
        left = sameTree(p.left,q.left)
        if left:
            return sameTree(p.right,q.right)
        else:
            return False