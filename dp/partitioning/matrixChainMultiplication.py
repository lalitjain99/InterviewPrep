"""
Given the dimension of a sequence of matrices in an array arr[], where the dimension of the ith matrix is (arr[i-1] * arr[i]), the task is to find the most efficient way to multiply these matrices together such that the total number of element multiplications is minimum.

Examples:

Input: arr[] = {40, 20, 30, 10, 30}
Output: 26000
Explanation:There are 4 matrices of dimensions 40×20, 20×30, 30×10, 10×30.
Let the input 4 matrices be A, B, C and D.
The minimum number of  multiplications are obtained by 
putting parenthesis in following way (A(BC))D.
The minimum is 20*30*10 + 40*20*10 + 40*10*30

Input: arr[] = {1, 2, 3, 4, 3}
Output: 30
Explanation: There are 4 matrices of dimensions 1×2, 2×3, 3×4, 4×3. 
Let the input 4 matrices be A, B, C and D.  
The minimum number of multiplications are obtained by 
putting parenthesis in following way ((AB)C)D.
The minimum number is 1*2*3 + 1*3*4 + 1*4*3 = 30

Input: arr[] = {10, 20, 30}
Output: 6000  
Explanation: There are only two matrices of dimensions 10×20 and 20×30. 
So there  is only one way to multiply the matrices, cost of which is 10*20*30

"""

# Matrix Chain Multiplication using Recursion:
# We can solve the problem using recursion based on the following facts and observations:

# Two matrices of size m*n and n*p when multiplied, they generate a matrix of size m*p and the number of multiplications performed are m*n*p.

# Now, for a given chain of N matrices, the first partition can be done in N-1 ways. For example, sequence of matrices A, B, C and D can be grouped as (A)(BCD), (AB)(CD) or (ABC)(D) in these 3 ways. 

# So a range [i, j] can be broken into two groups like {[i, i+1], [i+1, j]}, {[i, i+2], [i+2, j]}, . . . , {[i, j-1], [j-1, j]}.

# Each of the groups can be further partitioned into smaller groups and we can find the total required multiplications by solving for each of the groups.
# The minimum number of multiplications among all the first partitions is the required answer.
# Follow the steps mentioned below to implement the approach:

# Create a recursive function that takes i and j as parameters that determines the range of a group.
# Iterate from k = i to j to partition the given range into two groups.
# Call the recursive function for these groups.
# Return the minimum value among all the partitions as the required minimum number of multiplications to multiply all the matrices of this group.
# The minimum value returned for the range 0 to N-1 is the required answer.
import sys

maxint=int(1e9+7)

def matrixChainMultiplication(arr,i,j):
    if i >= j:
        return 0

    _min = maxint
    for k in range(i,j):

        temp = (matrixChainMultiplication(arr,i,k) + matrixChainMultiplication(arr,k+1,j) + arr[i-1]*arr[k]*arr[j])

        _min = min(temp,_min)

    return _min

arr = [1, 2, 3, 4, 3]

print(matrixChainMultiplication(arr,1,4))