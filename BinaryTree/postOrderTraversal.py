"""
145. Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]
Explanation:
Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
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

#Approach 1: Recursion
#Time Complexity:O(N) each node is traveled at least once
#Space Complexity:O(H)

def postOrder(root:TreeNode):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.val,end=" ")

#Approach 2: Using 2 stacks
#Time Complexity:O(N) each node is traveled at least once
#Space Complexity:O(N)
def postOrder_2stack(root:TreeNode):
    if root is None:
        return []
    result = []
    st1 = [root]
    st2 = []
    while st1:
        node = st1.pop()
        st2.append(node)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    while st2:
        node = st2.pop()
        result.append(node.val)
    
    return result

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, None, 8, None, 6, 7, 9]
    root = build_binary_tree(nodes)
    print("Post Order traversal using recursion",end=" ")
    postOrder(root)
    print()
    print("Post Order Traversal using 2 stacks",postOrder_2stack(root))
