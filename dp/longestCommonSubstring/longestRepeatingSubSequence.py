"""


Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.

The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B. For example, A = "xax" and B = "xax" then the index of first "x" must be different in the original string for A and B.

Example 1:

Input:
str = "axxzxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x z x y 
0 1 2 3 4 5

The longest subsequence is "xx". 
It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str 


subsequence B
x x
0 1  <-- index of subsequence B
------
2 4  <-- index of str 

We are able to use character 'x' 
(at index 2 in str) in both subsequences
as it appears on index 1 in subsequence A 
and index 0 in subsequence B.
"""
#Approach 1: Recursion

def longestRepeatingSubSequence(s,idx1,idx2):

    if idx1<0 or idx2<0:
        return 0
    
    if s[idx1] == s[idx2] and idx1!=idx2:
        return 1 + longestRepeatingSubSequence(s,idx1-1,idx2-1)
    
    else:
        return max(longestRepeatingSubSequence(s,idx1-1,idx2),longestRepeatingSubSequence(s,idx1,idx2-1))
    
s = "axxxy"
n = len(s)
print("Recursion: Longest Repeating Subsequence is ",longestRepeatingSubSequence(s,n-1,n-1))



# This problem is just the modification of Longest Common Subsequence problem. The idea is to find the LCS(str, str) where str is the input string with the restriction that when both the characters are same, they shouldn’t be on the same index in the two strings. 

def longest_repeating_subsequence(s):
    n = len(s)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
     
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if (s[i-1] == s[j-1] and i != j):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[n][n]

s = "axxzxy"
print("Tabulation: Longest Repeating Subsequence is ",longest_repeating_subsequence(s))