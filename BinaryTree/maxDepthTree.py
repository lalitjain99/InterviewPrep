"""104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104]."""
class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None 
        self.right = None 

def build_binary_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]

    i = 1
    while i < len(nodes):
        node = queue.pop(0)

        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root

#Approach : Recursive
#Time Complexity: O(N)
#Space Complexity: O(N)
def maxDepth(root:TreeNode):
    if root is None:
        return 0
    lh = maxDepth(root.left)
    rh = maxDepth(root.right)

    return 1 + max(lh,rh)

if __name__ == '__main__':
    nodes = [1, 2, 3, 4, 5, None, 8, None, 6, 7, 9]
    root = build_binary_tree(nodes)
    print(maxDepth(root))
