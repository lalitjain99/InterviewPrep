"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

#Approach 1: Recursion
# Time Complexity : O(2**n)  because for every idx we have 2 options
# Space Complexity : O(n)
def longestIncreasingSubsequence(nums,i,prev_i):

    #base condition
    if i == len(nums):
        return 0
    length  = 0 + longestIncreasingSubsequence(nums,i+1,prev_i)

    if (prev_i == -1 or nums[i]>nums[prev_i]):
        length =  max(length, 1 + longestIncreasingSubsequence(nums,i+1,i))
        
    return length

nums = [0,1,0,3,2,3]
print("Recursion: length of longest increasing subsequence is ",longestIncreasingSubsequence(nums,0,-1))

# def longestIncreasingSubsequence_var(nums,i,j):

#     #base condition
#     if j == len(nums):
#         return 0
#     length  = 0 + longestIncreasingSubsequence_var(nums,i,j+1)

#     if (i == 0 or nums[j]>nums[i]):
#         length =  max(length, 1 + longestIncreasingSubsequence_var(nums,j,j+1))
        
#     return length

# nums = [7,7,7,7,7,7,7]
# print("Recursion: length of longest increasing subsequence is ",longestIncreasingSubsequence_var(nums,0,1))

#Approach 2: Recursion with memoization
# Time Complexity : O(n*n)  because we are storing the sub-problems vales so for each n and previous idx problem is computed only once
# Space Complexity : O(n) + O(n)(n+1)
def longestIncreasingSubsequence_memo(nums,idx,prev_idx):

    #base condition
    if idx == len(nums):
        return 0
    dp[idx][prev_idx+1]  = 0 + longestIncreasingSubsequence_memo(nums,idx+1,prev_idx)

    if (prev_idx == -1 or nums[idx]>nums[prev_idx]):
        dp[idx][prev_idx+1] =  max(dp[idx][prev_idx+1], 1 + longestIncreasingSubsequence_memo(nums,idx+1,idx))
        
    return dp[idx][prev_idx+1]

nums = [10,9,2,5,3,7,101,18]
n = len(nums)
dp = [[-1 for _ in range(n+1)] for _ in range(n)]
print("Recursion with memoization: length of longest increasing subsequence is ",longestIncreasingSubsequence_memo(nums,0,-1))


#Approach 3: Tabulation
#Time Complexity: O(N*N)
#Space Complexity: O(N)
def longestIncreasingSubsequence_tab(nums):
    n = len(nums)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for idx in range(n-1,-1,-1):
        for prev_idx in range(idx-1,-2,-1):
            len_ = 0 + dp[idx+1][prev_idx+1]
            if prev_idx == -1 or nums[idx]> nums[prev_idx]:
                len_ = max(len_, 1+ dp[idx+1][idx+1])
        
            dp[idx][prev_idx + 1] = len_
    return dp[0][0]


nums = [10,9,2,5,3,7,101,18]         
print("Tabulation: length of longest increasing subsequence is ",longestIncreasingSubsequence_tab(nums))