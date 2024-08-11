# Given an integer array nums, find the subarray with the largest sum, and return its sum.

def maxSubArray( nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        curr_sum +=n
        if curr_sum <0:
            curr_sum = 0
        max_sum = max(max_sum,curr_sum)

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSubArray(nums))