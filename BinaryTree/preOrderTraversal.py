class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None

#Approach 1: Iterative using single stack
#Time Complexity: O(N)
#Space Complexity: O(h) where h is height of the tree 
def preOrder(root:TreeNode):
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res

#Approach 2: Recursive
#Time Complexity: O(N)
#Space Complexity: O(N) for ASS otherwise O(1)
def pre_order(root:TreeNode):
    if root is None:
        return
    print(root.val,end=" ")
    pre_order(root.left)
    pre_order(root.right)
