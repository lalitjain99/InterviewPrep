"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

"""
#Approach 1: Recursion

def uniquePathsWithObstacles(obstacleGrid: list[list[int]],m,n)-> int:

    if obstacleGrid[m][n] == 1:
        return 0
    if m == 1 or n == 1:
        return 1

    return uniquePathsWithObstacles(obstacleGrid,m-1,n) + uniquePathsWithObstacles(obstacleGrid,m,n-1)

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
m,n = 3,3

print(" number of unique paths with Obstacle using recursion", uniquePathsWithObstacles(obstacleGrid,m-1,n-1))


#Approach 2: Recursion with memoization

def uniquePathWithObstacles_Memo(obstacleGrid: list[list[int]],m,n)-> int:

    if obstacleGrid[m][n] == 1:
        dp[m][n] = 0
        return dp[m][m]
    if m == 1 or n == 1:
        dp[m][n] = 1
        return dp[m][n]
    
    dp[m][n] = uniquePathWithObstacles_Memo(obstacleGrid,m-1,n) + uniquePathWithObstacles_Memo(obstacleGrid,m,n-1)
    return dp[m][n]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
m,n = 3,3
dp = [[0 for _  in range(n)] for _ in range(m)]

print(" number of unique paths with Obstacle using recursion with memoization", uniquePathWithObstacles_Memo(obstacleGrid,m-1,n-1))


#Approach 3 : Tabulation 

def uniquePathWithObstacles_tab(obstacleGrid: list[list[int]])-> int:
    
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    #boundary condition
    #if there only 1 row and 1 column we need to check the value whether it is 0 or 1 
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

    #now we need to check first row till last column if any obstacle is present
    for i in range(1,n) :
        if obstacleGrid[0][i] == 0:
            dp[0][i] = dp[0][i-1]
    #similarly we need to check for first column
    for j in range(1,m):
        if obstacleGrid[j][0] == 0:
            dp[j][0] = dp[j-1][0]

    for i in range(1,n):
        for j in range(1,m):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]

obstacleGrid = [[0,0]]
print(" number of unique paths with Obstacle using tabulation", uniquePathWithObstacles_tab(obstacleGrid))

# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# m,n = 3,3