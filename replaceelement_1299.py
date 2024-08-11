# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

arr = [17,18,5,4,6,1]
#Output: [18,6,6,6,1,-1]

def replaceElements(arr: list[int]) -> list[int]:
    right_max = -1
    for i in range(len(arr)-1,-1,-1):
        temp_right_max = arr[i]
        arr[i] = right_max
        if temp_right_max > right_max:
            right_max = temp_right_max

    return arr

print(replaceElements(arr))
