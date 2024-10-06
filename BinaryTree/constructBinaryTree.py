"""What is Binary Tree?
Binary tree is a tree data structure(non-linear) in which each node can have at most two children which are referred to as the left child and the right child. 

The topmost node in a binary tree is called the root, and the bottom-most nodes are called leaves. A binary tree can be visualized as a hierarchical structure with the root at the top and the leaves at the bottom.

Representation of Binary Tree
Each node in a Binary Tree has three parts:

Data
Pointer to the left child
Pointer to the right child
"""

class TreeNode:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None

#first Initialize all nodes
first_node = TreeNode(2)
sec_node = TreeNode(3)
third_node = TreeNode(4)
fourth_node = TreeNode(5)

#now connect nodes
first_node.left = sec_node
first_node.right = third_node
sec_node.left = fourth_node

