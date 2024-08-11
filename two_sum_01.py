# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sums(nums: list[int], target: int) -> list[int]:

    nums_dict = {}

    for idx,num in enumerate(nums):
        diff = target - num
        if diff in nums_dict:
            return (nums_dict[diff],idx)
        else:
            nums_dict[num] = idx

nums = [2,7,11,15]
print(two_sums(nums=nums,target=9)) 

    