"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.


"""


def sumOfUnique(nums: list[int]) -> int:
    unique_element = {}
    for num in nums:
        if num in unique_element:
            unique_element[num] += 1
        else:
            unique_element[num] = 1
    print("uni_ele",unique_element)
    unique_element_sum = 0
    for key,value in unique_element.items():
        if value == 1:
            unique_element_sum += key
    
    return unique_element_sum

nums = [1,2,3,2]

print(sumOfUnique(nums))