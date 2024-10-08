"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


"""
#recursive solution
#Bottom up 

def lcs_recur(x:str,y:str,n,m):
    #boundary condition
    if n==0 or m== 0:
        return 0
    
    if x[n-1] == y[m-1]:
        return 1 + lcs_recur(x,y,n-1,m-1)
    else:
        return max(lcs_recur(x,y,n-1,m),lcs_recur(x,y,n,m-1))
    

text1 = "abcde"
text2 = "ace"
n=5
m=3
print("recursive approach",lcs_recur(x=text1,y=text2,n=n,m=m))


# recursive with memoization
#bottom up 

def lcs_memo(x:str,y:str,n,m,mtx):
    #base condition
    if n==0 or m== 0:
        return 0
    
    if mtx[n][m] != -1:
        return mtx[n][m]
    
    if x[n-1] == y[m-1]:
        mtx[n][m] = 1 + lcs_recur(x,y,n-1,m-1)
        return  mtx[n][m]
    else:
        mtx[n][m] = max(lcs_recur(x,y,n-1,m),lcs_recur(x,y,n,m-1))
        return mtx[n][m]

X = "AGGTAB"
Y = "GXTXAYB"

n = len(X)
m = len(Y)
dp = [[-1 for i in range(m + 1)]for j in range(n + 1)]

print("memoization approach", lcs_memo(x=X,y=Y,n=n,m=m,mtx=dp))

# top down approach
def lcs_tabulation(text1,text2):

    n = len(text1)
    m = len(text2)

    mtx = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(0,n+1):
        for j in range(0,m+1):
            if i== 0 or j == 0:
                mtx[i][j] = 0

            elif text1[i-1] == text2[j-1]:
                mtx[i][j] = 1 + mtx[i-1][j-1]

            else:
                mtx[i][j] = max(mtx[i-1][j], mtx[i][j-1])

    return mtx[n][m]


text1 = "abcde"
text2 = "ace"

print("tabulation approach", lcs_tabulation(text1,text2))
