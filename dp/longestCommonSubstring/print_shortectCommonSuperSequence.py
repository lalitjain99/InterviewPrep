"""
Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest super-sequence exists, print any one of them.
Examples: 
 

Input: X = "AGGTAB",  Y = "GXTXAYB"
Output: "AGXGTXAYB" OR "AGGXTXAYB" 
OR Any string that represents shortest
supersequence of X and Y

Input: X = "HELLO",  Y = "GEEK"
Output: "GEHEKLLO" OR "GHEEKLLO"
OR Any string that represents shortest 
supersequence of X and Y

"""
# We have already discussed below algorithm to find length of shortest super-sequence in previous post-
 

# Let X[0..m-1] and Y[0..n-1] be two strings and m and be respective 
# lengths.

# if (m == 0) return n;
# if (n == 0) return m;

# // If last characters are same, then add 1 to result and
# // recur for X[]
# if (X[m-1] == Y[n-1]) 
#     return 1 + SCS(X, Y, m-1, n-1);

# // Else find shortest of following two
# //  a) Remove last character from X and recur
# //  b) Remove last character from Y and recur
# else return 1 + min( SCS(X, Y, m-1, n), SCS(X, Y, m, n-1) );
# The following table shows steps followed by the above algorithm if we solve it in bottom-up manner using Dynamic Programming for strings X = “AGGTAB” and Y = “GXTXAYB”, 
 

# Shortest Supersequence Problem DP table

# Using the DP solution matrix, we can easily print shortest super-sequence of two strings by following below steps –
 

# We start from the bottom-right most cell of the matrix and 
# push characters in output string based on below rules-

#  1. If the characters corresponding to current cell (i, j) 
#     in X and Y are same, then the character is part of shortest 
#     supersequence. We append it in output string and move 
#     diagonally to next cell (i.e. (i - 1, j - 1)).

#  2. If the characters corresponding to current cell (i, j)
#     in X and Y are different, we have two choices -

#     If matrix[i - 1][j] > matrix[i][j - 1],
#     we add character corresponding to current 
#     cell (i, j) in string Y in output string 
#     and move to the left cell i.e. (i, j - 1)
#     else
#     we add character corresponding to current 
#     cell (i, j) in string X in output string 
#     and move to the top cell i.e. (i - 1, j)

#  3. If string Y reaches its end i.e. j = 0, we add remaining
#     characters of string X in the output string
#     else if string X reaches its end i.e. i = 0, we add 
#     remaining characters of string Y in the output string.



def print_scs(text1,text2,n,m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    i = n #represent row
    j = m #represents column
    scs = ''
    while i>0 and j>0:
        if text1[i-1] == text2[j-1]:
            scs += text1[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j]>dp[i][j-1]:   #if same 
            scs += text1[i-1]
            i -= 1
        else:
            scs += text2[j-1]
            j -= 1
    while i>0:
        scs += text1[i-1]
        i -= 1
    while j > 0:
        scs += text2[j-1]
        j -= 1
    scs = scs[::-1]
    return scs

text1 = "AGGTAB"
n=len(text1)
text2 = "GXTXAYB"
m = len(text2)
print(" shortest common superstring is",print_scs(text1,text2,n,m))

    