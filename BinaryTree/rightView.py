"""Right View of Binary Tree
Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right 
side. Return the right view as a list. 

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8

Examples :

Input:
       1
    /    \
   3      2
Output: 1 2
Input:
     10
    /   \
  20     30
 /   \
40  60 
Output: 10 30 60
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(Height of the Tree).

Constraints:
1 ≤ Number of nodes ≤ 105
0 ≤ Data of a node ≤ 105"""

#Approach: PreOrder Traverse with modification --> root-right-left
#Time Complexity: O(N)
#Space Complexity: O(H)
class TreeNode:
    def __init__(self,val:int) -> None:
        self.val = val 
        self.left = None
        self.right = None



def rightView(root:TreeNode,level:int,arr:list):
    if root is None:
        return 
    if level == len(arr):
        arr.append(root.val)
    rightView(root.right,level+1,arr)
    rightView(root.left,level+1,arr)


