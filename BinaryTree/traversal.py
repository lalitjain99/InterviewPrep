"""Traversal in Binary Tree involves visiting all the nodes of the binary tree. Tree Traversal algorithms can be classified 
broadly into two categories, DFS and BFS:

Depth-First Search (DFS) algorithms: DFS explores as far down a branch as possible before backtracking. It is implemented using 
recursion. The main traversal methods in DFS for binary trees are:

Preorder Traversal (current-left-right): Visits the node first, then left subtree, then right subtree.
Inorder Traversal (left-current-right): Visits left subtree, then the node, then the right subtree.
Postorder Traversal (left-right-current): Visits left subtree, then right subtree, then the node.


Breadth-First Search (BFS) algorithms: BFS explores all nodes at the present depth before moving on to nodes at the next 
depth level. It is typically implemented using a queue. BFS in a binary tree is commonly referred to as Level Order Traversal.
"""

class TreeNode:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None

def in_order_dfs(root):
    if root is None:
        return
    in_order_dfs(root.left)
    print(root.data, end= " ")
    in_order_dfs(root.right)

def pre_order_dfs(root):
    if root is None:
        return
    
    print(root.data, end= " ")
    pre_order_dfs(root.left)
    pre_order_dfs(root.right)

def post_order_dfs(root):
    if root is None:
        return
    
    post_order_dfs(root.left)
    post_order_dfs(root.right)
    print(root.data, end= " ")

def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end= " ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    # Creating the tree
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(5)

    print("In-order DFS: ", end='')
    in_order_dfs(root)
    print("\nPre-order DFS: ", end='')
    pre_order_dfs(root)
    print("\nPost-order DFS: ", end='')
    post_order_dfs(root)
    print("\nLevel order: ", end='')
    bfs(root)