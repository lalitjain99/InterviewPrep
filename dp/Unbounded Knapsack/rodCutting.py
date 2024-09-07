"""
Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: Consider 1-based indexing.

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.
Example 2:

Input:
N=8
Price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 
24
Explanation: 
The maximum obtainable value is 
24 by cutting the rod into 8 pieces 
of length 1, i.e, 8*price[1]= 8*3 = 24. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function cutRod() which takes the array A[] and its size N as inputs and returns the maximum price obtainable.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 1000
1 ≤ Ai ≤ 105

"""

#bottom up dp approach

def cutRodBottomUp(n,price):
    mat = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j== 0:
                mat[i][j] = 0
            elif i > j:
                mat[i][j] = mat[i-1][j]
            else:
                mat[i][j] = max(price[i-1] + mat[i][j-i], mat[i-1][j])
                
    return mat[n][n]

N=8
price = [3, 5, 8, 9, 10, 17, 17, 20]

print("Bottom Up DP",cutRodBottomUp(n=N,price=price))


#recursive approach

def cutRod(n,price):
    i=1
    if n==0:
        return 0
    if i<=n:
        i +=1
        max_profit = max(price[i-1] + cutRod(n-i,price),cutRod(n-i,price))
    else:
        i+=1
        max_profit = cutRod(n-i,price)

    return max_profit

N=8
price = [3, 5, 8, 9, 10, 17, 17, 20]

print(cutRod(n=N,price=price))



    

