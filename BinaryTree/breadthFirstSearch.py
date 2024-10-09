"""102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
#Approach 1: One queue to traverse curr level node and another to store next level nodes
#Time Complexity: O(N)
#Space Complexity: O(N)
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def levelOrder(root:TreeNode):
    if root is None:
        return []
    result = []
    queue = [root]
    next_queue = []
    level = []
    while queue:
        for root in queue:
            level.append(root.val)
            if root.left:
                next_queue.append(root.left)
            if root.right:
                next_queue.append(root.right)
        result.append(level)
        queue = next_queue
        next_queue = []
        level = []
    
    return result

#Approach 2: Singe queue to maintain current and next level
#Time Complexity: O(N)
#Space Complexity: O(N)
from collections import deque
def levelOrder(root:TreeNode):
    if root is None:
        return []

    queue = deque([root])
    result = []
    while queue:
        lvl_size = len(queue)
        curr_lvl = []
        for _ in range(lvl_size):
            node = queue.popleft()
            curr_lvl.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(curr_lvl)
    
    return result
