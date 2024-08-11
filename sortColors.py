"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
"""
# order
#  red -- 0
#  white -- 1
#  blue -- 2

def sortColors(nums:list[int])-> list[int]:
    left,idx,right = 0,0,len(nums)-1
    while idx <= right:
        if nums[idx] == 0:
            nums[left],nums[idx] = nums[idx],nums[left]
            left +=1
            idx +=1
            print("nums in zero check",nums)
        elif nums[idx] == 2:
            nums[right],nums[idx] = nums[idx],nums[right]
            right -=1
            print("nums in two check",nums)
        else:
            idx += 1
    return nums

nums = [2,0,2,1,1,0]
print(sortColors(nums))



