"""
Given a set of non-negative integers and a value sum, the task is to check if there is a subset of the given set whose sum is equal to the given sum. 

Examples: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
Explanation: There is no subset that add up to 30.

"""

def subsetSum(N:int,arr:list,sum:int):
    #initialize the matrix with all false of size (N+1)*(sum+1)
    mtx = [[False for i in range(sum+1)] for j in range(N+1)]

    #check boundary conditions
    for i in range(N+1):
        mtx[i][0] = True
    for i in range(1,sum+1):
        mtx[0][i] = False

    print(mtx)
    for i in range(1,N+1):
        for j in range(1,sum+1):
            if arr[i-1]<= j:
                mtx[i][j] = (mtx[i-1][j-arr[i-1]]) or mtx[i-1][j]
            else:
                mtx[i][j] = mtx[i-1][j]
    return mtx[N][sum]

N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 9

print(subsetSum(N,arr,sum))