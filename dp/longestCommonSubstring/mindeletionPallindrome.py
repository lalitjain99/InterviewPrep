"""
Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. 

Note: The order of characters should be maintained. 

Examples : 

Input : "aebcbda"
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string
Input : "geeksforgeeks"
Output : 8

"""

def minDeletion(s1):
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
    
    return n-dp[n][n]

s1 = "geeksforgeeks"

print("Minimum number of deletion required",minDeletion(s1))