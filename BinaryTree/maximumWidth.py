"""Maximum Width of Tree
Difficulty: EasyAccuracy: 63.27%Submissions: 81K+Points: 2
Given a Binary Tree, find the maximum width of it. Maximum width is defined as the maximum number of nodes at any level.

Examples:

Input:
       1
     /    \
    2      3

Output: 2
Explanation: On the first level there is only one node 1. On the second level there are two nodes 2, 3 clearly it is the 
maximum number of nodes at any level

Input:
        10
      /     \
    20      30
   /    \
  40    60
Output: 2
Explanation: There is one node on level 1(10) There is two node on level 2(20, 30) There is two node on level 3(40, 60) 
Hence the answer is 2
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(width of the tree).

Constraints:
1 <= number of nodes<= 105
0 <= node->data <= 105"""

from collections import deque


class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def maxWidth(root:TreeNode):
    if not root:
        return 0
    
    max_width = 0
    queue = deque([root])
    level_idx = deque([1])
    while queue:
        level_size = len(queue)
        max_width = max(max_width,(max(level_idx)-min(level_idx)+1))
        for _ in range(level_size):
            node = queue.popleft()
            level = level_idx.popleft()
            if node.left:
                level_idx.append(2*(level-1)+1)
                queue.append(node.left)

            if node.right:
                level_idx.append(2*(level-1)+2)
                queue.append(node.right)

    return max_width