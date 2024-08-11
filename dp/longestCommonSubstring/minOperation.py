"""
Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

Example 1:

Input: str1 = "heap", str2 = "pea"
Output: 3
Explanation: 2 deletions and 1 insertion.
p and h deleted from heap. Then, p is inserted at the beginning.
One thing to note, though p was required yet it was removed/deleted first from its position and then it is inserted to some other position. Thus, p contributes one to the 
deletion_count and one to the insertion_count.
Example 2:

Input : str1 = "geeksforgeeks"
str2 = "geeks"
Output: 8
Explanation: 8 deletions, i.e. remove all characters of the string "forgeeks".
Your Task:
You don't need to read or print anything. Your task is to complete the function minOperations() which takes both strings as input parameter and returns the minimum number of operation required.

Expected Time Complexity: O(|str1|*|str2|)
Expected Space Complexity: O(|str1|*|str2|)

Constraints:
1 ≤ |str1|, |str2| ≤ 1000
"""
#An efficient approach uses the concept of finding the length of the longest common subsequence of the given two sequences.

# Algorithm: 

# str1 and str2 be the given strings.
# m and n be their lengths respectively.
# len be the length of the longest common subsequence of str1 and str2
# minimum number of deletions minDel = m – len (as we only need to delete from str1 because we are reducing it to str2)
# minimum number of Insertions minInsert = n – len (as we are inserting x in str1 , x is a number of characters in str2 which are not taking part in the string which is longest common subsequence )


def minOperations(self, s1, s2):
		#code here
        n = len(s1)
        m = len(s2)
		
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
		
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
		            
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
		 
        deletion_count = n - dp[n][m]
        insertion_count = m - dp[n][m]
        
        return deletion_count+insertion_count