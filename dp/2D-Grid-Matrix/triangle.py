"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104

"""
# def minTotal(triangle,lastIndex):
#     row = len(triangle)
    
#     #check boundary condition
#     if row == 1:
#         lastIndex = 0
#         return triangle[row-1][0]
    
#     minCost = min((triangle[row-1][lastIndex] + minTotal(triangle[:-1],lastIndex)),(triangle[row-1][lastIndex+1] + minTotal(triangle[:-1],lastIndex)))

#     return minCost
    

# triangle = [ [ 2 ], [ 3, 9 ], [ 1, 6, 7 ] ]

# print(minTotal(triangle,0))
#Approach 1: recursion
# Time Complexity: O(2N*N) where N = number of rows and M = number of columns
# Auxiliary Space: O(N)

def minTotal(triangle,row,col):

    if row > len(triangle):
        return 0
    
    minCost = triangle[row-1][col-1] + min(minTotal(triangle,row+1,col-1),minTotal(triangle,row+1,col))

    return minCost

triangle = [ [ 2 ], [ 3, 9 ], [ 1, 6, 7 ] ]

print("minimum total to reach last row in triangle using recursion",minTotal(triangle,1,1))


#Approach 2: Recursion with memoization
# Time Complexity: O(N*M) where N = number of rows and M = number of columns

# Auxiliary Space: O(N2)

def minTotal_Memo(triangle,row,col):
    if row > len(triangle):
        return 0
    
    if dp[row-1][col-1] != -1:
        return dp[row-1][col-1]
    
    dp[row-1][col-1]= triangle[row-1][col-1] + min(minTotal(triangle,row+1,col-1),minTotal(triangle,row+1,col))

    return dp[row-1][col-1]

triangle = [ [ 2 ], [ 3, 9 ], [ 1, 6, 7 ] ]
dp = [[-1]*len(triangle)]*len(triangle)
print("minimum total to reach last row in triangle using recursion with memoization",minTotal_Memo(triangle,1,1))


#Approach 3 : Tabulation

def minTotal_tab(triangle):

    n = len(triangle)
    
    # Start at the second last row of the triangle
    for i in range(n-2, -1, -1):
        # Iterate over each number in the current row
        for j in range(len(triangle[i])):
            # Add the minimum of the two adjacent numbers from the next row
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    
    # Return the value at the top of the triangle
    return triangle[0][0]

triangle = [ [ 2 ], [ 3, 9 ], [ 1, 6, 7 ] ]
print("minimum total to reach last row in triangle using tabulation",minTotal_tab(triangle))


    