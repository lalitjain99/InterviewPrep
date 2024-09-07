"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
#Approach 1: Recursion with memoization
#Time Complexity: O(2**N) + O(2**N)-->O(2**N)
#Space Complexity: O(N) + O(N)-->N
def robLinear(houses,idx,lastIdx):
    if idx < lastIdx:
        return 0
    if idx == lastIdx:
        return houses[idx]
    
    noRob = 0 + robLinear(houses,idx-1,lastIdx)
    rob = houses[idx] + robLinear(houses,idx-2,lastIdx)

    return max(noRob,rob)

def rob(houses: list[int]) -> int:

    n = len(houses)

    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0],houses[1])

    case1 = robLinear(houses,n-1,1)
    case2 = robLinear(houses,n-2,0)

    return max(case1,case2)

houses = [1,2,3,1]
print("Recursion: Maximum money robbed with circular setup will be ",rob(houses))

#Approach 2: Recursion with memoization
#Time Complexity: O(N) + O(N)-->N
#Space Complexity: ASS (O(N) + O(N)) + O(N)-->O(N)
def robLinear_memo(houses,idx,lastIdx,dp):
        if idx < lastIdx:
            return 0
        if idx == lastIdx:
            return houses[idx]
        if dp[idx] != -1:
            return dp[idx]
        
        noRob = 0 + robLinear_memo(houses,idx-1,lastIdx,dp)
        rob = houses[idx] + robLinear_memo(houses,idx-2,lastIdx,dp)
        dp[idx] = max(noRob,rob)
        return dp[idx]

def rob_memo(houses: list[int]) -> int:

    n = len(houses)

    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0],houses[1])
    dp = [-1]*(n)
    case1 = robLinear_memo(houses,n-1,1,dp)
    dp = [-1]*n
    case2 = robLinear_memo(houses,n-2,0,dp)

    return max(case1,case2)

houses = [1,2,3,1]
print("Recursion with memoization: Maximum money robbed with circular setup will be ",rob_memo(houses))

def rob_tab(houses: list[int]) -> int:

    n = len(houses)

    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0],houses[1])
    if n == 3:
        return max(houses[2],max(houses[0],houses[1]))
    
    else:
        dp1 = [-1]*(n-1)
        dp1[0] = houses[0]
        dp1[1] = max(houses[0],houses[1])
        for i in range(2,n-1):
            dp1[i] = max(dp1[i-1],(dp1[i-2]+houses[i]))
        
        dp2 = [-1]*(n-1)
        dp2[0] = houses[1]
        dp2[1] = max(houses[1],houses[2])
        for i in range(2,n-1):
            dp2[i] = max(dp2[i-1],(dp2[i-2]+houses[i+1]))

        return max(dp1[n-2],dp2[n-2])
    
houses = [1,2,3,1]
print("Tabulation: Maximum money robbed with circular setup will be ",rob_tab(houses))

def rob_spaceOptimized(nums):
    prev,prev2 = 0,0
    for n in nums[:-1]:
        temp = max(prev2,(prev+n))
        prev = prev2
        prev2 = temp
    
    rob1,rob2 = 0,0

    for n in nums[1:]:
        temp = max(rob2,(rob1+n))
        rob1 = rob2
        rob2 = temp

    return max(prev2,rob2)

nums = [1,2,3,1,5]
print("Space Optimized: Maximum money robbed with circular setup will be", rob_spaceOptimized(nums))



# Approach 1: Recursion

# def rob_linear(houses, start, end):
#     """
#     Recursively calculates the maximum amount of money that can be robbed from a linear set of houses.
    
#     :param houses: List of integers representing the amount of money in each house.
#     :param start: Starting index of the houses to consider.
#     :param end: Ending index of the houses to consider.
#     :return: Maximum amount of money that can be robbed.
#     """
#     # Base case: No houses to rob.
#     if start > end:
#         return 0
    
#     # Base case: Only one house to rob.
#     if start == end:
#         return houses[start]
    
#     # Recursive case: Choose between robbing the current house and skipping the next,
#     # or skipping the current house.
#     rob_current = houses[start] + rob_linear(houses, start + 2, end)
#     skip_current = rob_linear(houses, start + 1, end)
    
#     # Return the maximum amount possible.
#     return max(rob_current, skip_current)

# def rob_circular(houses):
#     """
#     Calculates the maximum amount of money that can be robbed from houses arranged in a circle.
    
#     :param houses: List of integers representing the amount of money in each house.
#     :return: Maximum amount of money that can be robbed.
#     """
#     n = len(houses)
    
#     # Base case: If there are no houses, return 0.
#     if n == 0:
#         return 0
    
#     # Base case: If there is only one house, return the amount in that house.
#     if n == 1:
#         return houses[0]
    
#     # Case 1: Rob houses from the first to the second-to-last.
#     case1 = rob_linear(houses, 0, n - 2)
    
#     # Case 2: Rob houses from the second to the last.
#     case2 = rob_linear(houses, 1, n - 1)
    
#     # Return the maximum amount from both cases.
#     return max(case1, case2)

# # Example usage
# nums = [1,2, 3, 1]
# print("rob circular ",rob_circular(nums))  

# def rob2(nums,n,lastSelected):

#     if lastSelected:
#         if n < 1:
#             return 0
        
#     else:
#         if n <= 1:
#             return 0
        
#     lastAllowed,lastNotAllowed = rob2(nums,n-1,True), (rob2(nums,n-2,False) + nums[n-1])
#     return max(lastAllowed,lastNotAllowed)

# nums = [1,2,3,1]
# n=len(nums)
# print("house rob 2 using recursion",rob2(nums,n,False))

# The recursive function you wrote aims to solve the circular house robbery problem, but there are a few issues that need to be addressed for it to work correctly:

# Handling the Circular Condition: Your current implementation doesn't correctly address the circular condition of the problem. It assumes that the houses are in a linear order. The recursion should account for the fact that if the first house is robbed, the last one cannot be, and vice versa.

# Base Case for Recursion: The base cases are not fully accounting for the constraints given by the lastSelected flag. The flag should help determine if the last house in the sequence is allowed to be robbed.

# Recursive Case Logic: The logic for deciding when to add the value of the current house is slightly misaligned with the rules of the problem.