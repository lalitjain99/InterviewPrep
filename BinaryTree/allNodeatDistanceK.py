"""863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all 
nodes that have a distance k from the target node.

You can return the answer in any order.
 

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:

Input: root = [1], target = 1, k = 3
Output: []

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000"""

from collections import deque


class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def findParentNode(self,node:TreeNode):
        if not node:
            return []
        parent_map = {}
        queue = deque([node])
        parent_map[node] = None
        while queue:
            lvl_size = len(queue)
            for _ in range(lvl_size):
                node = queue.popleft()
                if node.left:
                    parent_map[node.left] = node
                    queue.append(node.left)
                if node.right:
                    parent_map[node.right] = node
                    queue.append(node.right)
        return parent_map

def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
    p_map = self.findParentNode(root)
    queue = deque([target])
    visited_node = {}
    visited_node[target] = True
    curr_k = 0
    while queue:
        q_length = len(queue)
        if curr_k == k:
            break
        for _ in range(q_length):
            node = queue.popleft()
            if node.left and node.left not in visited_node:
                queue.append(node.left)
                visited_node[node.left] = True
            if node.right and node.right not in visited_node:
                queue.append(node.right)
                visited_node[node.right] = True
            if p_map[node] and p_map[node] not in visited_node:
                queue.append(p_map[node])
                visited_node[p_map[node]] = True
        
        curr_k += 1
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node.val)
    
    return ans
