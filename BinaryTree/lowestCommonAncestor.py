"""LCA in Binary Tree
Given a Binary Tree with all unique values and two nodes value, n1 and n2. The task is to find the lowest common ancestor 
of the given two nodes. We may assume that either both n1 and n2 are present in the tree or none of them are present.

LCA: It is the first common ancestor of both the nodes n1 and n2 from bottom of tree.

Example 1:

Input:
n1 = 2 , n2 = 3  
       1 
      / \ 
     2   3
Output: 1
Explanation:
LCA of 2 and 3 is 1.

Example 2:

Input:
n1 = 3 , n2 = 4
           5    
          /    
         2  
        / \  
       3   4
Output: 2
Explanation:
LCA of 3 and 4 is 2. 

Example 3:

Input:
n1 = 5 , n2 = 4
           5    
          /    
         2  
        / \  
       3   4
Output: 5
Explanation:
LCA of 5 and 4 is 5. 
Your Task:
You don't have to read, input, or print anything. Your task is to complete the function lca() that takes nodes, n1, and n2 as 
parameters and returns the LCA node as output. 

Expected Time Complexity:O(N).
Expected Auxiliary Space:O(Height of Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
1 ≤ Data of a node ≤ 105"""

class TreeNode:
    def __init__(self,val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def findNodePath(node:TreeNode,path:list,x:int):
    if not node:
        return False
    
    path.append(node.val)

    if node.val == x:
        return True
    
    if findNodePath(node.left,path,x) or findNodePath(node.left,path,x):
        return True
    path.pop()
    return False

def LCA(root:TreeNode,n1,n2):

    n1_path = []
    n2_path = []
    findNodePath(root,n1_path,n1)
    findNodePath(root,n2_path,n2)

    i = 0
    while i < len(n1_path) and i < n2_path:
        if n1_path[i] == n2_path[i]:
            break
        i +=1

    return TreeNode(n1_path[i])

