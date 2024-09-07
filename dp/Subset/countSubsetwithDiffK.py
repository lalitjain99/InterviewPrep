"""
Given an array arr[] of size N and a given difference diff, the task is to count the number of partitions that we can perform such that the difference between the sum of the two subsets is equal to the given difference.

Note: A partition in the array means dividing an array into two parts say S1 and S2 such that the union of S1 and S2 is equal to the original array and each element is present in only of the subsets.

Examples:

Input: N = 4, arr[] = [5, 2, 6, 4], diff = 3
Output: 1
Explanation: We can only have a single partition which is shown below:
{5, 2} and {6, 4} such that S1 = 7 and S2 = 10 and thus the difference is 3

Input: N = 5, arr[] = [1, 2, 3, 1, 2], diff = 1
Output: 5
Explanation: We can have five partitions which is shown below
{1, 3, 1} and {2, 2} – S1 = 5, S2 = 4
{1, 2, 2} and {1, 3} – S1 = 5, S2 = 4
{3, 2} and {1, 1, 2} – S1 = 5, S2 = 4
{1, 2, 2} and {1, 3} – S1 = 5, S2 = 4
{3, 2} and {1, 1, 2} – S1 = 5, S2 = 4
"""
#Approach 1: Recursion

def countSubset(nums,n,targetSum):
    # if targetSum == 0:
    #     return 1
    
    if n == 0:
        if targetSum == 0 and nums[n] == 0:
            return 2
        return 1 if nums[n] == targetSum else 0
    
    noPick = countSubset(nums,n-1,targetSum)
    pick = 0
    if nums[n]<= targetSum:
        pick = countSubset(nums,n-1,targetSum-nums[n])

    return pick + noPick

def countSubsetWithDiff(nums,diff):
    n = len(nums)
    total = 0
    for i in nums:
        total += i

    targetSum = (total+diff)/2

    return countSubset(nums,n-1,targetSum)

nums = [1, 2, 3, 1, 2]
diff = 1

print("Recursion: number of subset with given difference {a} is".format(a=diff),countSubsetWithDiff(nums,diff))

#Approach 3: Tabulation

def countSubsetWithDiff_tab(nums,diff):
    n = len(nums)
    total = 0
    for i in nums:
        total += i

    if (total+diff)%2 != 0:
        return 0
    
    targetSum = (total+diff)//2

    dp = [[0]*(targetSum +1) for _ in range((n+1))]
    
    #base conditions
    dp[0][0] = 1
    #if sum is zero , then we can return True 
    # for i in range(n+1):
    #     dp[i][0] = True

    #if number of element is zero and sum greater than 0 then return False
    # for i in range(1,targetSum+1):
    #     dp[0][i] = False

    for i in range(1,n+1):
        for j in range(0,targetSum+1):
            dp[i][j] = dp[i-1][j]
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                dp[i][j] %= 10**9 + 7
    
    return dp[len(nums)][targetSum]

nums = [1, 2, 3, 1, 2]
diff = 1

print("Tabulation: number of subset with given difference {a} is".format(a=diff),countSubsetWithDiff_tab(nums,diff))
