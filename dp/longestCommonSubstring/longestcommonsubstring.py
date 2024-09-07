"""
Given two strings. The task is to find the length of the longest common substring.


Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.
Example 2:

Input: S1 = "ABC", S2 "ACB", n = 3, m = 3
Output: 1
Explanation: The longest common substrings
are "A", "B", "C" all having length 1.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestCommonSubstr() which takes the string S1, string S2 and their length n and m as inputs and returns the length of the longest common substring in S1 and S2.


Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).


Constraints:
1<=n, m<=1000
"""

#Recursive approach

def substring_recur(text1,text2,n,m,result):
    
    # boundary condition
    if n == -1 or m == -1:
        return result
    
    if text1[n-1] == text2[m-1]:
        
        return  substring_recur(text1,text2,n-1,m-1,result+1)
    else:
        result = max(result,max(substring_recur(text1,text2,n-1,m,0),substring_recur(text1,text2,n,m-1,0)))
        return result
    
text1 = "ABCDGH"
text2 = "ACDGHR"
n = len(text1)
m = len(text2)
result = 0
print("recursive approach", substring_recur(text1,text2,n,m,result))


#Recursive with Memo


def lc_substring_memo(x,y,n,m,dp,result):
    
    #boundary Conditions 
    if n == 0 or m == 0:
        return result
    
    if dp[n][m] != -1:
        return dp[n][m]
    
    if x[n-1] == y[m-1]:
        dp[n][m] = lc_substring_memo(x,y,n-1,m-1,dp,result+1)
        return dp[n][m]
    
    else:
        dp[n][m] = max(result,max(lc_substring_memo(text1,text2,n-1,m,dp,0),lc_substring_memo(text1,text2,n,m-1,dp,0))) 
        return dp[n][m]
    
x = "ABCDGH"
y = "ACDGHR"

n = len(x)
m = len(y)
dp = [[-1 for i in range(m + 1)]for j in range(n + 1)]
result = 0
print('longest common substring with memoization',lc_substring_memo(x,y,n,m,dp,result))

#top down approach
def lc_substring_dp(x,y,n,m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    count = 0
    for i in range(n+1):
        for j in range(m+1):
            if i ==0 or j == 0:
                dp[i][j] = 0
            elif x[i-1] == y[j-1]:
                dp[i][j] = 1+ dp[i-1][j-1]
                count = max(count,dp[i][j])
            else:
                dp[i][j] = 0

    return count

x = "ABCDGH"
y = "ACDGHR"

n = len(x)
m = len(y)
print('longest common substring with top down dp',lc_substring_dp(x,y,n,m))