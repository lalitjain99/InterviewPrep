"""
Given a set of non-negative integers and a value sum, the task is to check if there is a subset of the given set whose sum is equal to the given sum. 

Examples: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
Explanation: There is no subset that add up to 30.

"""
#Approach 1: Recursion
# For the recursive approach, there will be two cases. 

# Consider the ‘last’ element to be a part of the subset. Now the new required sum = required sum – value of ‘last’ element.
# Don’t include the ‘last’ element in the subset. Then the new required sum = old required sum.
# In both cases, the number of available elements decreases by 1.

def isSubsetSum(nums,n,targetSum):
    #base condition
    #if no element if present then we can not have subset
    if n < 1:
        return False
    #if target sum is 0 then we have a subset 
    if targetSum == 0:
        return True
    
    if nums[n-1] <= targetSum:
        isPresent = isSubsetSum(nums,n-1,targetSum-nums[n-1]) or isSubsetSum(nums,n-1,targetSum)
    else:
        isPresent = isSubsetSum(nums,n-1,targetSum)
    
    return isPresent

nums = [3, 34, 4, 12, 5, 2]
n = 6
targetSum = 30
print("is subset with target sum present using recursion",isSubsetSum(nums,n,targetSum))
    
#Approach 2: Recursion with memoization

def isSubsetSum_memo(nums,n,targetSum):
    if n<1:
        return False
    if targetSum == 0:
        return True
    if dp[n-1] != -1:
        return dp[n-1]
    
    if nums[n-1]>targetSum:
        dp[n-1] = isSubsetSum_memo(nums,n-1,targetSum)
        return dp[n-1]
    else:
        dp[n-1] = isSubsetSum_memo(nums,n-1,targetSum) or isSubsetSum_memo(nums,n-1,targetSum-nums[n-1])
        return dp[n-1]
    
nums = [3, 34, 4, 12, 5, 2]
n = 6
targetSum = 30
dp = [-1]*n

print("is subset with target sum present using recursion with memoization",isSubsetSum_memo(nums,n,targetSum))

#Approach 3: Tabulation 

def isSubsetSum_tab(nums,targetSum):
    #create a 2D dp array having size equal to size of arr and target sum
    dp = [[-1]*(targetSum +1) for _ in range((len(nums)+1))]
    
    #base conditions
    #if sum is zero , then we can return True 
    for i in range(len(nums)+1):
        dp[i][0] = True

    #if number of element is zero and sum greater than 0 then return False
    for i in range(1,targetSum+1):
        dp[0][i] = False

    for i in range(1,len(nums)+1):
        for j in range(1,targetSum+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    return dp[len(nums)][targetSum]


nums = [3, 34, 4, 12, 5, 2]
targetSum = 30
print("is subset with target sum present using tabulation",isSubsetSum_tab(nums,targetSum))