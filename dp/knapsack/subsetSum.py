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
#recursive approach 
def isSubsetSumRecursive(N,arr,sum):
    # check for boundary conditions
    if N==0:
        return False
    if sum == 0:
        return True
    
    if arr[N-1]> sum:
        return isSubsetSumRecursive(N-1,arr,sum)

    return (isSubsetSumRecursive(N-1,arr,sum) or isSubsetSumRecursive(N-1,arr,sum-arr[N-1]))

N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 9
print("bottom up recursive approach ", isSubsetSumRecursive(N,arr,sum))

#Bottom up recursive with memoization

def isSubsetSumRecurMemo(N,arr,sum):
    #initialize a matrix with size (N+1)*(Sum+1)
    mtx =[[-1 for i in range(sum+1)] for j in range(N+1)]

    #check for boundary conditions:
    if (N == 0):
        return False
    
    if (sum == 0):
        return True

    if mtx[N-1][sum] != -1:
        return mtx[N-1][sum]
    
    if arr[N-1]>sum:
        mtx[N-1][sum] =  isSubsetSumRecurMemo(N-1,arr,sum)
        return mtx[N-1][sum]
    else:
        mtx[N-1][sum] = isSubsetSumRecurMemo(N-1,arr,sum) or isSubsetSumRecurMemo(N-1,arr,sum-arr[N-1])
        return mtx[N-1][sum]

N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 9
print("bottom up recursive with memo  ", isSubsetSumRecurMemo(N,arr,sum))
    



#top down dynamic programming approach
def isSubsetSumBottomUp(N,arr,sum):
    #initialize a matrix with all False value
    mtx  = [[False for i in range(sum+1)] for i in range(N+1)]
    # print("initial matrix",mtx)

    #check for boundary case 
    for i in range(N+1):
        mtx[i][0] = True

    for j in range(sum+1):
        mtx[0][j] = True

    #matrix after boundary case handling
    # print("Matrix after boundary case handling",mtx)

    for i in range(1,N+1): #i will handle the row i.e number of values
        for j in range(1,sum+1): #j will handle the column i.e. current sum value
            if j < arr[i-1]:
                mtx[i][j] = mtx[i-1][j]   # this will tell we have excluded this number , but are we able to create subset even after excluding --> since j is same in both side of the equation so we are checking till previous number are we able to form any subset
            if j >= arr[i-1]:
                mtx[i][j] = (mtx[i-1][j] or mtx[i-1][j-arr[i-1]]) # here we have 2 options whether to include this number or not... mtx[i-1][j] will tell if we are excluding this number are we able to find any subset mtx[i-1][j-arr[i-1]] this equation will check if we include this current number then is difference of current sum - current number = remaining subset sum exists or not

    return mtx[N][sum]





N = 6
arr = [3, 34, 4, 12, 5, 2]
sum = 9

print("Bottom up approach dynamic programming",isSubsetSumBottomUp(N,arr,sum))