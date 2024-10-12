"""2385. Amount of Time for Binary Tree to Be Infected

You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from 
the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 
Example 1:
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.

Example 2:
Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 
Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree."""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self) -> None:
        self.val = val 
        self.left = None
        self.right = None

def findParentNode(self,node,target):
        target_node = TreeNode()
        queue = deque([node])
        parent_map = {}
        parent_map[node] = None
        while queue:
            curr_node = queue.popleft()
            if curr_node.val == target:
                target_node = curr_node

            if curr_node.left:
                parent_map[curr_node.left] = curr_node
                queue.append(curr_node.left)
            if curr_node.right:
                parent_map[curr_node.right] = curr_node
                queue.append(curr_node.right)
                
            
                
        return parent_map,target_node

def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    if not root:
        return 0
    
    p_map,target_node = self.findParentNode(root,start)
    # code here
    # print(type(target))
    queue = deque([target_node])
    visited_node = {}
    visited_node[target_node] = True
    time = -1
    while queue:
        qSize = len(queue)
        # print(qSize)
        for _ in range(qSize):
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
        time +=1
        
    return time