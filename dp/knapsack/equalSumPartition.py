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

def canPartition(nums:list)-> bool:
    sum = 0
    for i in nums:
        sum += i
    
    if sum%2 != 0:
        return False

    mtx = [[False for i in range((sum//2)+1)] for j in range(len(nums)+1)]

    for i in range(len(nums)+1):
        mtx[i][0] = True

    for j in range(1,sum//2+1):
        mtx[0][j] = False

    for i in range(1,len(nums)+1):
        for j in range(1, sum//2+1):
            if nums[i-1]<=j:
                mtx[i][j] = mtx[i-1][j-nums[i-1]] or mtx[i-1][j]
            else:
                mtx[i][j] = mtx[i-1][j]
    return mtx[len(nums)][sum//2]

nums = [1,5,11,5]
print(canPartition(nums=nums))