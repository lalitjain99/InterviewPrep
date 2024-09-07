"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
#Approach 1: Recursion
#Time Complexity: (2**N)
#Space Complexity: (N)
def rob(nums,idx):
    if idx<0:
        return 0
    if idx == 0:
        return nums[0]

    notRob = 0 + rob(nums,idx-1)
    robbed = nums[idx] + rob(nums,idx-2)

    return max(notRob,robbed)

nums = [2,7,9,3,1]
n = len(nums)
print("Recursion: Maximum money robbed will be ",rob(nums,n-1))

#Approach 2: Recursion with tabulation
#Time Complexity: (N)
#Space Complexity: (N)
def rob_memo(nums,idx):
    if idx<0:
        return 0
    if idx == 0:
        return nums[0]
    if dp[idx] != -1:
        return dp[idx]
    notRob = 0 + rob_memo(nums,idx-1)
    robbed = nums[idx] + rob_memo(nums,idx-2)

    dp[idx] = max(notRob,robbed)

    return dp[idx]

nums = [2,7,9,3,1]
n = len(nums)
dp = [-1]*n
print("Recursion with memo: Maximum money robbed will be ",rob_memo(nums,n-1))
#Approach 3: tabulation top-down 
# Create an extra space DP array to store the sub-problems.
# Tackle the following basic cases, 
# If the length of the array is 0, print 0. 
# If the length of the array is 1, print the first element. 
# If the length of the array is 2, print a maximum of two elements.
# Update dp[0] as array[0] and dp[1] as maximum of array[0] and array[1]
# Traverse the array from the second element (2nd index) to the end of the array.
# For every index, update dp[i] as a maximum of dp[i-2] + array[i] and dp[i-1], this step defines the two cases if an element is selected then the previous element cannot be selected and if an element is not selected then the previous element can be selected.
# Print the value dp[n-1]

def rob_tab(nums,n):
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0],nums[1])
    
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,n):
        dp[i] = max((dp[i-2]+ nums[i]),dp[i-1])

    return dp[n-1]

nums = [1,2,3,1]
n = 4
print("Tabulation: maximum money robbed ",rob_tab(nums,n))

#Approach 2: space optimized
def rob_spaceOptimized(nums,n):
    prev,prev2 = 0,0
    for n in nums:
        temp = max(prev2,(prev+n))
        prev = prev2
        prev2 = temp
    return prev2

nums = [1,2,3,1]
n = 4
print("Space optimized : maximum money robbed ",rob_spaceOptimized(nums,n))

#Approach 3: recursive solution
# def rob_recur(nums,n):
#     if n < 0 :
#         return 0
#     else:
#         money = max(rob_recur(nums,n-1),(rob_recur(nums,n-2)+nums[n]))
#         return money

# nums = [2,1,4,9]
# n = 4
# print("maximum robbed money using recursion",rob_recur(nums,n-1))

# #Approach 4: recursive with memoization
# dp = [0]*n
# def rob_memo(nums,n):
#     if n < 0:
#         return 0
#     if dp[n] != -1:
#         return dp[n]
#     else:
#         dp[n] = max(rob_memo(nums,n-1),rob_memo(nums,n-2)+ nums[n])
#         return dp[n-1]

# nums = [2,1,4,9]
# n = 4
# print("maximum robbed money using memoization",rob_recur(nums,n-1))

