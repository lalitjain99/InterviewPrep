"""
You are given an integer array nums, an integer array queries, and an integer x.

For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.

Return an integer array answer containing the answers to all queries.

 
Example 1:

Input: nums = [1,3,1,7], queries = [1,3,2,4], x = 1

Output: [0,-1,2,-1]
"""

def occurrencesOfElement( nums: list[int], queries: list[int], x: int) -> list[int]:
    output= []
    x_freq_nums = {}
    freq = 0
    for i in range(len(nums)):
        if nums[i] == x:
            freq += 1
            x_freq_nums[freq] = i
    # print("x_freq",x_freq_nums)
    for query in queries:
        if query > freq:
            output.append(-1)
        else:
            output.append(x_freq_nums[query])
    return output

nums = [1,3,1,7]
queries = [1,3,2,4]
x = 1
print(occurrencesOfElement(nums,queries,x))

