"""103. Binary Tree Zigzag Level Order Traversal
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100"""

class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def zigZagTraversal(root:TreeNode):
    if root is None:
        return []
    res = []
    queue = deque([root])
    left_to_right = True
    while queue:
        lvl_size = len(queue)
        curr_lvl = []
        for _ in range(lvl_size):
            node = queue.popleft()
            if left_to_right:
                curr_lvl.append(node.val)
            else:
                curr_lvl.insert(0,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(curr_lvl)
    
    return res