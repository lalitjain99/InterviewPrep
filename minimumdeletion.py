"""
You are given a 0-indexed integer array nums. The array nums is beautiful if:

nums.length is even.
nums[i] != nums[i + 1] for all i % 2 == 0.
Note that an empty array is considered beautiful.

You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

Return the minimum number of elements to delete from nums to make it beautiful.

"""

def minDeletion(nums: list[int]) -> int:
    deletion = 0
    num_len_after_deletion = 0

    for i in range(len(nums)-1):
        if (num_len_after_deletion % 2 ==0) and (nums[i] == nums[i+1]):
            deletion +=1
        else:
            num_len_after_deletion += 1

    num_len_after_deletion +=1    

    deletion += num_len_after_deletion & 1

    return deletion

nums = [1,1,2,2,3,3]
print(minDeletion(nums))