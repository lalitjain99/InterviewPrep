"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

"""

#Approach 1: Recursive 

def isSubsetSum(nums,n,targetSum):
    
    if n == 1:
        return False
    if targetSum == 0:
        return True
    
    if nums[n-1] > targetSum:
        return isSubsetSum(nums,n-1,targetSum)
    
    else:
        return isSubsetSum(nums,n-1,targetSum-nums[n-1]) or isSubsetSum(nums,n-1,targetSum)
    
def isEqualSumPartition(nums):

    total = 0
    for i in nums:
        total += i

    if total%2 != 0:
        return False
    else:
        return isSubsetSum(nums,len(nums),total//2)
    
nums = [1,2,3,5]
print("is partition equal subset sum using recursion",isEqualSumPartition(nums))


#Approach 2: Recursive with memoization

def isSubsetSum_memo(nums,n,targetSum,dp):
    
    if n == 1:
        return False
    if targetSum == 0:
        return True
    if dp[n-1][targetSum] != -1:
        return dp[n-1][targetSum]
    if nums[n-1] > targetSum:
        dp[n-1][targetSum] = isSubsetSum_memo(nums,n-1,targetSum,dp)
        return dp[n-1][targetSum]
    
    else:
        dp[n-1][targetSum] = isSubsetSum_memo(nums,n-1,targetSum-nums[n-1],dp) or isSubsetSum_memo(nums,n-1,targetSum,dp)
        return dp[n-1][targetSum]
    
def isEqualSumPartition_memo(nums):

    total = 0
    for i in nums:
        total += i

    if total%2 != 0:
        return False
    else:
        dp = [[-1]*((total//2) + 1)]*len(nums)
        return isSubsetSum_memo(nums,len(nums),total//2,dp)
    
nums = [1,2,3,5]

print("is partition equal subset sum using recursion with memoization",isEqualSumPartition_memo(nums))

#Approach 3: Tabulation

def isEqualSubsetSumPartition_tab(nums):
    total = 0

    for i in nums:
        total += i

    if total % 2 != 0:
        return False

    #create a 2D dp array having size equal to size of arr and target sum
    dp = [[-1]*(total +1) for _ in range((len(nums)+1))]
    
    #base conditions
    #if sum is zero , then we can return True 
    for i in range(len(nums)+1):
        dp[i][0] = True

    #if number of element is zero and sum greater than 0 then return False
    for i in range(1,total+1):
        dp[0][i] = False

    for i in range(1,len(nums)+1):
        for j in range(1,total+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    
    return dp[len(nums)][total]


nums = [1,5,11,5]

print("is partition equal subset sum using tabulation",isEqualSubsetSumPartition_tab(nums))