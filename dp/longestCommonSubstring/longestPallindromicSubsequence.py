"""
The Longest Palindromic Subsequence (LPS) is the problem of finding a maximum-length subsequence of a given string that is also a Palindrome.

Input: S = “GEEKSFORGEEKS”
           "SKEEGROFSKEEG"
        lcs = 
Output: 5
Explanation: The longest palindromic subsequence we can get is of length 5. There are more than 1 palindromic subsequences of length 5, for example: EEKEE, EESEE, EEFEE, …etc.

Input: S = “BBABCBCAB”
Output: 7
Explanation: As “BABCBAB” is the longest palindromic subsequence in it. “BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the longest ones.

"""
# Following is a general recursive solution with all cases handled. 

# Case1: Every single character is a palindrome of length 1
# L(i, i) = 1 (for all indexes i in given sequence)
# Case2: If first and last characters are not same
# If (X[i] != X[j])  L(i, j) = max{L(i + 1, j), L(i, j – 1)} 
# Case3: If there are only 2 characters and both are same
# Else if (j == i + 1) L(i, j) = 2  
# Case4: If there are more than two characters, and first and last characters are same
# Else L(i, j) =  L(i + 1, j – 1) + 2 

def longestPallindromicSubsequene(s1):
    reverse_s1 = s1[::-1]
    n = len(s1)
    # m = len(reverse_s1)

    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == reverse_s1[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][n]

S = "GEEKSFORGEEKS"

print("length of longest pallindrome string is ", longestPallindromicSubsequene(s1=S))
        