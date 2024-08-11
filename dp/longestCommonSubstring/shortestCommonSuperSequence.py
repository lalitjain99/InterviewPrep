"""
Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.

Examples : 

Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.

"""

# Method 1: This problem is closely related to longest common subsequence problem.
# Below are steps.

# Find Longest Common Subsequence (lcs) of two given strings. For example, lcs of “geek” and “eke” is “ek”. 
# Insert non-lcs characters (in their original order in strings) to the lcs found above, and return the result. So “ek” becomes “geeke” which is shortest common supersequence.
# Let us consider another example, str1 = “AGGTAB” and str2 = “GXTXAYB”. LCS of str1 and str2 is “GTAB”. Once we find LCS, we insert characters of both strings in order and we get “AGXGTXAYB”
# How does this work? 

# We need to find a string that has both strings as subsequences and is the shortest such string. If both strings have all characters different, then result is sum of lengths of two given strings. If there are common characters, then we don’t want them multiple times as the task is to minimize length. Therefore, we first find the longest common subsequence, take one occurrence of this subsequence and add extra characters. 

# Length of the shortest supersequence  
# = (Sum of lengths of given two strings) 
# - (Length of LCS of two given strings) 

def shortestCommonSuperSequence(text1,text2,n,m):

    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    return (n+m-dp[n][m])

text1 = "AGGTAB"
n=len(text1)
text2 = "GXTXAYB"
m = len(text2)
print("length of shortest common superstring is",shortestCommonSuperSequence(text1,text2,n,m))