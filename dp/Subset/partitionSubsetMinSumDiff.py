"""
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example: 

Input: arr[] = {1, 6, 11, 5}
Output: 1
Explanation: S1 = {1, 5, 6}, sum = 12, S2 = {11}, sum = 11, Absolute Difference (12 – 11) = 1

Input: arr[] = {1, 5, 11, 5}
Output: 0
Explanation: S1 = {1, 5, 5}, sum = 11, S2 = {11}, sum = 11, Absolute Difference (11 – 11) = 0

"""
#Approach 1: Recursion
def minDiff(nums,n):
    return "hello world"


#Approach 3: Tabulation
def minSumDiffSubsetPartition(nums):
    n = len(nums)
    total = 0
    for i in nums:
        total += i

    dp = [[-1 for i in range(total+1)] for j in range(n+1)]

    #base condition
    #if target sum is 0 we can always return True 
    for i in range(n+1):
        dp[i][0] = True

    #if number of element is zero we can always return False
    for i in range(1,total+1):
        dp[0][i] = False

    for i in range(1,n+1):
        for j in range(1,total+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

    pseudo_s1 = []
    for j in range(total//2 + 1):
        if dp[n][j]:
            pseudo_s1.append(j)

    minDiff = float("inf")

    for sum in pseudo_s1:
        minDiff = min(minDiff,(total-2*sum))

    return minDiff

nums = [1, 6, 11, 5]
print("minimum sum difference for subset partition is ", minSumDiffSubsetPartition(nums))
                      



