"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

def searchInsert(nums: list[int], target: int) -> int:
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

nums = [1,3,5,6]
target = 5
print(searchInsert(nums,target))