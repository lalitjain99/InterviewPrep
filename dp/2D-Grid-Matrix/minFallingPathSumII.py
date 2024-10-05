"""
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:

Input: grid = [[7]]
Output: 7
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""
#Approach 1: Recursion
#Time complexity:
#Space Complexity

class Solution:
    def path(self,grid,row,lastCol):
        n  = len(grid)
        if row == (n-1):
            lastRowMinPoints = float("inf")
            for col in range(n):
                if col != lastCol:
                    points = grid[row][col]
                    lastRowMinPoints = min(points,lastRowMinPoints)
            return lastRowMinPoints

        minPoints = float("inf")
        for col in range(n):
            if col != lastCol:
                points = grid[row][col] + self.path(grid,row+1,col)
                minPoints = min(points,minPoints)

        return minPoints

    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        return self.path(grid,0,n+1)





#Approach 3: Tabulation
#Time Complexity: O(N*N*N) + O(N) --> O(N**3)
#Space Complexity: O(N*N) 
def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        dp = [[0 for _ in range(n)] for _ in range(n) ]

        dp[0] = grid[0]

        
        
        for row in range(1,n):
            for lastCol in range(n):
                minPoints = float("inf")
                for col in range(n):
                    if col != lastCol:
                        points = grid[row][lastCol] + dp[row-1][col]
                        minPoints = min(points,minPoints)
                
                dp[row][lastCol] = minPoints

        minPoints = float("inf")
        for col in range(n):
            minPoints = min(minPoints,dp[n-1][col])
        return minPoints