"""
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property)

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 
Example 2:

Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Your Task:
Complete the function knapSack() which takes maximum capacity W, weight array wt[], value array val[], and the number of items n as a parameter and returns the maximum possible value you can get.

Expected Time Complexity: O(N*W).
Expected Auxiliary Space: O(N*W)

Constraints:
1 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ v[i] ≤ 1000
"""

# def recursive_knapsack(W:int,wt:list,val:list,N:int):

#     #boundary conditions
#     if W==0 or N==0:
#         return 0
#     #check if current wt is less than or equal target Weight
#     if wt[N-1] <= W:
#         profit = max((val[N-1] + recursive_knapsack(W-wt[N-1],wt,val,N-1)),recursive_knapsack(W,wt,val,N-1))
#     else:
#         profit = recursive_knapsack(W,wt,val,N-1)
    
#     return profit

# N = 3
# W = 4
# values = [1,2,3]
# weight = [4,5,1]

# print(recursive_knapsack(W,wt=weight,val=values,N=N,))

def top_down_knapsack(W, wt, val, n):
    #create a matrix initialize it with -1 of size n*W 
    mtx = [[-1 for i in range(W+1)] for j in range(n+1) ]

    #check boundary conditions
    for i in range(W):
        mtx[0][i] = 0

    # print(mtx)

    for i in range(n):
        mtx[i][0] = 0

    # print(mtx)
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                mtx[i][j] = max((val[i-1]+mtx[i-1][j-wt[i-1]]),mtx[i-1][j])
            else:
                mtx[i][j] = mtx[i-1][j]
    
    return mtx[n][W]

N = 3
W = 4
values = [1,2,3]
weight = [4,5,1]

print(top_down_knapsack( W=W, wt=weight, val=values, n=N))