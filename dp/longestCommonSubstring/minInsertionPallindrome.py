"""

"""
#Approach 1: Recursion
class Solution:
    def lcs(self,s1,s2,idx1,idx2):

        if idx1<0 or idx2<0:
            return 0

        if s1[idx1] == s2[idx2]:
            return 1 + self.lcs(s1,s2,idx1-1,idx2-1)

        return max(self.lcs(s1,s2,idx1,idx2-1),self.lcs(s1,s2,idx1-1,idx2))

    def minInsertions(self, s: str) -> int:

        s2 = s[::-1]
        n = len(s)
        longestPalindrome = self.lcs(s1=s,s2=s2,idx1=n-1,idx2=n-1)

        return n-longestPalindrome

#Approach 2: recursion with Memoization
#Time Complexity: O(N**2) --> size of dp (N**N) + execute function which O(1)
#Space Complexity: O(N*N) +O(N) --> O(N*N)
class Solution:
    def lcs(self,s1,s2,idx1,idx2,dp):

        if idx1<0 or idx2<0:
            return 0

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]

        if s1[idx1] == s2[idx2]:
            dp[idx1][idx2] = 1 + self.lcs(s1,s2,idx1-1,idx2-1,dp)
            return dp[idx1][idx2]

        dp[idx1][idx2] = max(self.lcs(s1,s2,idx1,idx2-1,dp),self.lcs(s1,s2,idx1-1,idx2,dp))
        return dp[idx1][idx2]

    def minInsertions(self, s: str) -> int:

        s2 = s[::-1]
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        longestPalindrome = self.lcs(s1=s,s2=s2,idx1=n-1,idx2=n-1,dp=dp)

        return (n-longestPalindrome)
    
#Approach 3: Tabulation
def minInsertion(s1):
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
s = "leetcode"
print("Tabulation: Minimum number of insertion required are ",minInsertion(s))