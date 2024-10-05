"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

"""

#Approach 1: Recursion
#Time Complexity: O(3**N+3**M)
#Space Complexity: O(N+M)

def minDistance(word1,word2,idx1,idx2):

    if idx1<0:
        return idx2 + 1
    
    if idx2<0:
        return idx1 + 1
    
    if word1[idx1] == word2[idx2]:
        return 0 + minDistance(word1,word2,idx1-1,idx2-1)
    
    insert = 1 + minDistance(word1,word2,idx1,idx2-1)
    delete = 1 + minDistance(word1,word2,idx1-1,idx2)
    replace = 1 + minDistance(word1,word2,idx1-1,idx2-1)

    return min(insert,delete,replace)

word1, word2 = "intention", "execution"
n1 = len(word1)
n2 = len(word2)
print("Recursion: Minimum number of operation needed to convert word1 to word2 is",minDistance(word1,word2,n1-1,n2-1))

# Approach 2: Recursion with memoization

def minDistance_memo(word1,word2,idx1,idx2):
    if idx1<0:
        return idx2 + 1
    
    if idx2<0:
        return idx1 + 1
    
    if dp[idx1][idx2] != -1:
        return dp[idx1][idx2]
    
    if word1[idx1] == word2[idx2]:
        dp[idx1][idx2] = 0 + minDistance(word1,word2,idx1-1,idx2-1)
        return 
    
    insert = 1 + minDistance(word1,word2,idx1,idx2-1)
    delete = 1 + minDistance(word1,word2,idx1-1,idx2)
    replace = 1 + minDistance(word1,word2,idx1-1,idx2-1)
    dp[idx1][idx2] = min(insert,delete,replace)
    return  dp[idx1][idx2]

word1, word2 = "intention", "execution"
n1 = len(word1)
n2 = len(word2)
dp = [[-1 for _ in range(n2)] for _ in range(n1)]
print("Recursion with memoization: Minimum number of operation needed to convert word1 to word2 is",minDistance(word1,word2,n1-1,n2-1))


#Tabulation

def minDistance_tab(word1,word2):
    pass
