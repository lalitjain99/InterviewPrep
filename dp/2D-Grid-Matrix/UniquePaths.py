"""
The problem is to count all unique possible paths from the top left to the bottom right of a M X N matrix with the constraints that from each cell you can either move only to the right or down

Examples: 

Input:  M = 2, N = 2
Output: 2
Explanation: There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)

Input:  M = 2, N = 3
Output: 3
Explanation: There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2)

"""

#Approach 1: Recursion
# Create a recursive function with parameters as row and column index
# Call this recursive function for N-1 and M-1
# In the recursive function
# If N == 1 or M == 1 then return 1
# else call the recursive function with (N-1, M) and (N, M-1) and return the sum of this
# Print the answer

def numberOfUniquePaths(m, n):
    # If either given row number is first
    # or given column number is first
    if m == 0 or n == 0:
            return 0
    
    if(m == 1 and n == 1):
        return 1

    # If diagonal movements are allowed
    # then the last addition
    # is required.
    return numberOfUniquePaths(m-1, n) + numberOfUniquePaths(m, n-1)

print("Recursion: number of unique paths to reach m-1,n-1 ", numberOfUniquePaths(3,7))


#Approach 2: Recursion with memoization
m,n=3,3
dp = [[0 for i in range(n+1)] for j in range(m+1)]

def uniquePathMemo(m,n):

    if (m == 1 or n == 1):
        dp[m][n] = 1
        return dp[m][n]
    
    if dp[m][n] == 0:
        dp[m][n] = uniquePathMemo(m-1,n) + uniquePathMemo(m,n-1)
    
    return dp[m][n]

print("number of unique paths to reach m-1,n-1 using recursion with memoization are",uniquePathMemo(m,n))

#Approach 3: tabulation (top-down)
def uniquePath_tab(m,n):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    #check boundary condition
    #if only row or only column is given then there is no way to reach bottom 
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m][n]

print("Tabulation: number of unique paths to reach m-1,n-1 ",uniquePath_tab(m,n))
    
            




    


