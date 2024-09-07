"""
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.

Examples: 

Input: arr[] = {1, 2, 3, 3}, X = 6 
Output: 3 
All the possible subsets are {1, 2, 3}, 
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1 
Output: 4 

"""

#Approach 1: Recursion

def countSubset(nums,n,targetSum):
    
    if n == 1:
        if (targetSum ==0 and nums[n-1] == 0):
            return 2
        return 1 if nums[n-1] == targetSum else 0
    #if target sum is 0 then we have a subset 
    
    noPick = countSubset(nums,n-1,targetSum)
    # pick = 0
    if nums[n-1] <= targetSum:
        pick =  countSubset(nums,n-1,targetSum-nums[n-1]) 
        
    
    return pick +  noPick
        


nums = [1, 2, 3, 3]
n = 4
targetSum = 6
print("Recursion : count of subset with target sum {k} is".format(k=targetSum),countSubset(nums,n,targetSum))

#Approach 2: Recursion with memoization

def countSubset_memo(nums,n,targetSum):
    
    if n == 1:
        if (targetSum ==0 and nums[n-1] == 0):
            return 2
        return 1 if nums[n-1] == targetSum else 0
    #if target sum is 0 then we have a subset 

    if dp[n-1][targetSum] != -1:
        return dp[n-1][targetSum]
    
    noPick = countSubset_memo(nums,n-1,targetSum)
    pick = 0
    if nums[n-1] <= targetSum:
        pick =  countSubset_memo(nums,n-1,targetSum-nums[n-1]) 
        
    dp[n-1][targetSum] = pick +  noPick
        
    
    return dp[n-1][targetSum]
        


nums = [1, 2, 3, 3]
n = 4
targetSum = 6
dp = [[-1]*(targetSum+1)]*(n+1)
print("Recursion with memoization: count of subset with target sum {k} is".format(k=targetSum),countSubset_memo(nums,n,targetSum))

#Approach 3: Tabulation 

def countSubset_tab(nums,targetSum):
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
        for j in range(0,targetSum+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
    
    return dp[len(nums)][targetSum]

nums = [1, 2, 3, 3]
targetSum = 6
print("Tabulation method: Number of subset with sum {a}".format(a=targetSum),countSubset_tab(nums,targetSum))