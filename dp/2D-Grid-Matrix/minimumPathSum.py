"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
#Approach 1: Recursion
# Define a 2D list t to store the minimum path sums for each cell, initialized to -1.
# Start from the bottom-right corner of the grid and recursively compute the minimum path sum to each cell.
# Recursive Function:

# Base Cases:
# If the cell is at the top-left corner, return its value as the minimum path sum.
# If the cell indices are out of bounds, return infinity (a very large value).
# Memoization:
# If the minimum path sum for a cell is already computed (i.e., t[m][n] != -1), return the stored value.
# Recursive Calculation:
# Compute the minimum path sums for the cell directly above and to the left.
# Update the cell's value in t with the minimum of the sums from the top and left plus the cell's own value.
# Result:

# The result for the bottom-right corner of the grid will be the minimum path sum from the top-left to bottom-right.
# Complexity
# Time Complexity:
# O(m * n), where m is the number of rows and n is the number of columns in the grid. Each cell is computed only once and stored.

# Space Complexity:
# O(m * n) for the memoization table t, plus the recursion stack space which can be up to O(m + n) in the worst case.

maxInt = float('inf')
def minPathSum(grid,row,col):
    # print("row",row)
    # print("col",col)
    # m = len(grid)
    # n = len(grid[0])

    #check boundary condition
    if row <= 0 or col <= 0:
        return maxInt
    
    if row == 1 and col == 1:
        return grid[row-1][col-1] 
    

    minCost = min((grid[row-1][col-1] + minPathSum(grid,row-1,col)),(grid[row-1][col-1] + minPathSum(grid,row,col-1)))
    return minCost

grid = [[1,2,3],[4,5,6]]
row = len(grid)
col = len(grid[0])
print("minimum cost path using recursion",minPathSum(grid,row,col))

#Approach 2: Recursion with tabulation

def minPathSum_Memo(grid,row,col):

    #check boundary condition
    if row <= 0 or col <= 0:
        return maxInt
    
    if row ==0 and col == 0:
        dp[row-1][col-1] = grid[row-1][col-1]
        return dp[row-1][col-1]
    
    if dp[row-1][col-1] != -1:
        return dp[row-1][col-1]
    
    dp[row-1][col-1] = min((grid[row-1][col-1] + minPathSum(grid,row-1,col)),(grid[row-1][col-1] + minPathSum(grid,row,col-1)))

    return dp[row-1][col-1]

grid = [[1,2,3],[4,5,6]]
row = len(grid)
col = len(grid[0])
dp = [[-1 for _ in range(col)] for _ in range(row)]
print("minimum cost path using recursion with memoization",minPathSum_Memo(grid,row,col))


#Approach 3: Tabulation

def minPathSum_tab(grid):
    row = len(grid)
    col = len(grid[0])

    dp = [[-1]*col for _ in range(row)]

    dp[0][0] = grid[0][0]

    #if only 1 row is given
    for i in range(1,col):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    #if only 1 col is given
    for j in range(1,row):
        dp[j][0] = dp[j-1][0] + grid[j][0]

    for i in range(1,row):
        for j in range(1,col):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
            
    return dp[row-1][col-1]




grid = [[1,2,3],[4,5,6]]

print("minimum cost path using recursion with tabulation",minPathSum_tab(grid))