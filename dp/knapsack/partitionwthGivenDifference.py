"""
Given an array arr, partition it into two subsets(possibly empty) such that each element must belong to only one subset. Let the sum of the elements of these two subsets be S1 and S2. 
Given a difference d, count the number of partitions in which S1 is greater than or equal to S2 and the difference between S1 and S2 is equal to d. Since the answer may be large return it modulo 109 + 7.

Example 1:

Input:
n = 4
d = 3
arr[] =  { 5, 2, 6, 4}
Output: 1
Explanation:
There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.
Example 2:

Input:
n = 4
d = 0 
arr[] = {1, 1, 1, 1} 
Output: 6 
Explanation:
we can choose two 1's from indices {0,1}, {0,2}, {0,3}, {1,2}, {1,3}, {2,3} and put them in S1 and remaning two 1's in S2.
Thus there are total 6 ways for partition the array arr. 
Your Task:
You don't have to read input or print anything. Your task is to complete the function countPartitions() which takes the integer n and d and array arr and returns the count of partitions.

Expected Time Complexity: O( n*sum(arr))
Expected Space Complexity: O( sum(arr))

Constraint:
1 <= n <= 500
0 <= d  <= 25000
0 <= arr[i] <= 50
"""
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

    for i in range(1,N+1): #i will handle the row i.e current number of values
        for j in range(0,sum+1): #j will handle the column i.e. current sum value
            if j >= arr[i-1]:
                mtx[i][j] = (mtx[i-1][j] + mtx[i-1][j-arr[i-1]])%mode# here we have 2 options whether to include this number or not... mtx[i-1][j] will tell if we are excluding this number are we able to find any subset mtx[i-1][j-arr[i-1]] this equation will check if we include this current number then is difference of current sum - current number = remaining subset sum exists or not
            if j < arr[i-1]:
                mtx[i][j] = mtx[i-1][j]   # this will tell we have excluded this number , but are we able to create subset even after excluding --> since j is same in both side of the equation so we are checking till previous number are we able to form any subset     

    return mtx[N][sum]

def countPartitions(n:int,diff:int,arr:list)-> int:
    subset_sum = 0
    for i in arr:
        subset_sum += i

    required_sum = (diff + subset_sum)//2
    return countSubsetSum(N=n,arr=arr,sum=required_sum)


n = 4
d = 3
arr =  [5, 2, 6, 4] 

print(countPartitions(n=n,diff=d,arr=arr))