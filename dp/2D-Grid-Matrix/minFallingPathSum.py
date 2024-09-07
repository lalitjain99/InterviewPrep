"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""

#Approach 1: Recursion
maxInt = float("inf")
def minFallingPath(matrix,row,col,n):
    #boundary and out of bound condition based on column
    if col > n-1 or col < 0:
        return maxInt
    # boundary condition based on row
    if row > n-1:
        return 0
    
    minCost = matrix[row][col] + min(minFallingPath(matrix,row+1,col-1,n),minFallingPath(matrix,row+1,col,n),minFallingPath(matrix,row+1,col+1,n))

    return minCost
matrix = [[-19,57],[-40,-5]]
cost = [-1]*len(matrix)
for i in range(len(matrix)):
    cost[i] = minFallingPath(matrix,0,i,len(matrix))

print("minimum falling path using recursion ",min(cost))
# print("minimum falling path using recursion ",minFallingPath(matrix,0,1,3))

#Approach 2 : recursion with memoization

def minFallingPath_memo(matrix,row,col):
    if col > len(matrix)-1 or col < 0:
        return maxInt
    # boundary condition based on row
    if row > len(matrix)-1:
        return 0
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    dp[row][col] = matrix[row][col] + min(minFallingPath_memo(matrix,row+1,col-1),minFallingPath_memo(matrix,row+1,col),minFallingPath_memo(matrix,row+1,col+1))

    return dp[row][col]

matrix = [[-19,57],[-40,-5]]
dp = [[-1]*len(matrix)]*len(matrix)
cost = [-1]*len(matrix)
for i in range(len(matrix)):
    cost[i] = minFallingPath_memo(matrix,0,i)

print("minimum falling path using recursion with memoization ",min(cost))

#Approach 3 : tabulation(top down)

def minFallingPath_tab(matrix):
    #base condition
    if len(matrix)==1:
            return min(matrix[0])
    ans = float('inf')
    for i in range(1,len(matrix)):
        print(i)
        for j in range(len(matrix)):
            print("matrix before iteration",matrix)
            down = matrix[i][j] + matrix[i-1][j]
            if j>0:
                leftDiagonal = matrix[i][j] + matrix[i-1][j-1]
            else:
                leftDiagonal = maxInt
            
            if j<len(matrix)-1:
                rightDiagonal = matrix[i][j] + matrix[i-1][j+1]
            else:
                rightDiagonal = maxInt

            matrix[i][j] = min(down,leftDiagonal,rightDiagonal)
            print("matrix after iteration",matrix)
            if i == (len(matrix)-1):
                ans = min(ans,matrix[i][j])

    return ans

matrix = [[2,1,3],[6,5,4],[7,8,9]]
print("minimum falling path using recursion with tabulation ",minFallingPath_tab(matrix))


def minFallingPathSum(self, m) -> int:
        if len(m)==1:
            return min(m[0])
        dp = [[-1 for i in range(len(m[0]))] for ii in range(len(m))]
        x = len(m)
        y = len(m[0])
        ans = float('inf')
        for i in range(y):
            dp[x-1][i]= m[x-1][i]
        for i in range(x-2,-1,-1):
            for j in range(y):
                t1 = dp[i+1][j-1] if j>0 else float('inf')
                t2 = dp[i+1][j] 
                t3 = dp[i+1][j+1] if j<=y-2 else float('inf')
                dp[i][j] = min([t1,t2,t3])+m[i][j]
                if i == 0:
                    ans = min(ans,dp[0][j])
        return ans