"""94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:

Example 3:
Input: root = []
Output: []

Example 4:

Input: root = [1]

Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
#Approach 1: Recursive Solution
#Time Complexity: O(N)
#Space Complexity: O(H) ASS

class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def inOrderTraversal(self, root: TreeNode) -> list[int]:
        l1 = []
        def inOrder(node):
            if node is None:
                return []
            inOrder(node.left)
            l1.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return l1

#Approach 2 : Iterative 
#Time Complexity: O(N)
#Space Complexity: O(H)

def inOrder(root:TreeNode):
    if root is None:
        return []
    result = []
    curr = root
    st = []
    while True:
        if curr is not None:
            st.append(curr)
            curr = curr.next 
        else:
            if not st:
                break
            node = st.pop()
            result.append(node.val)
            node = node.right 
    return result

         