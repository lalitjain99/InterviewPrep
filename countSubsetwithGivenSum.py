"""
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.

Examples: 

Input: arr[] = {1, 2, 3, 3}, X = 6 
Output: 3 
All the possible subsets are {1, 2, 3}, 
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1 
Output: 4 
"""
#top-down recursive dynamic approach
def countSubsetSumRecur(N,arr,sum):
    #check for boundary conditions
    if N==0:
        return 0
    if sum == 0 :
        return 1
    if arr[N-1]<=sum:
        count = countSubsetSumRecur(N-1,arr,sum) + countSubsetSumRecur(N-1,arr,sum-arr[N-1])
        return count
    else:
        count = countSubsetSumRecur(N-1,arr,sum)
        return count

arr = [9,7,0 ,3, 9, 8, 6, 5, 7, 6]
sum = 31
N = 10
print("top down recursive approach",  countSubsetSumRecur(N=N,arr=arr,sum=sum))

def countSubsetSum(N,arr,sum):
    #initialize a matrix with all False value inner list comprehension will handle number of columns and outer will handle number of rows
    mtx  = [[0 for j in range(sum+1)] for i in range(N+1)]
    # print("initial matrix",mtx)
    mode = 100000007
    #check for boundary case 
    for i in range(N+1):
        mtx[i][0] = 1

    for j in range(1,sum+1):
        mtx[0][j] = 0

    #matrix after boundary case handling
    # print("Matrix after boundary case handling",mtx)
    
    #i will handle the row i.e current number of values
    for i in range(1,N+1): 
        #j will handle the column i.e. current sum value !!Notice here that sum starts from 0 because there is possibility that array contains zero so we need to cater those subset as well
        for j in range(0,sum+1): 
            if j >= arr[i-1]:
                # here we have 2 options whether to include this number or not... mtx[i-1][j] will tell if we are excluding this number are we able to find any subset mtx[i-1][j-arr[i-1]] this equation will check if we include this current number then is difference of current sum - current number = remaining subset sum exists or not
                mtx[i][j] = (mtx[i-1][j] + mtx[i-1][j-arr[i-1]])%mode
            if j < arr[i-1]:
                # this will tell we have excluded this number , but are we able to create subset even after excluding --> since j is same in both side of the equation so we are checking till previous number are we able to form any subset
                mtx[i][j] = mtx[i-1][j]   

    return mtx[N][sum]


arr = [9,7,0 ,3, 9, 8, 6, 5, 7, 6]
sum = 31
N = 10
print(countSubsetSum(N=N,arr=arr,sum=sum))