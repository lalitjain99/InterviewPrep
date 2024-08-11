"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

def isSubsequence(s1,s2):
    n = len(s1)
    m = len(s2)

    mtx = [[-1 for i in range(m+1)] for j in range(n+1)]

    for i in range(0,n+1):
        for j in range(0,m+1):
            if i== 0 or j == 0:
                mtx[i][j] = 0

            elif s1[i-1] == s2[j-1]:
                mtx[i][j] = 1 + mtx[i-1][j-1]

            else:
                mtx[i][j] = max(mtx[i-1][j], mtx[i][j-1])

    return True if n==mtx[n][m] else False

s1,s2 = "abc","ahbgdc"
print(isSubsequence(s1,s2))
s1,s2 = "axc", "ahbgdc"
print(isSubsequence(s1,s2))