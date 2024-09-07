"""
Given a set of N items, each with a weight and a value, represented by the array w and val respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.

Input: 
N = 4
W = 8
val[] = {6, 1, 7, 7}
wt[] = {1, 3, 4, 5}
Output: 
48
Explanation: 
The optimal choice is to pick the 1st element 8 times.

"""
# Approach 1: Recursive 

def knapsack_with_duplicates_recursive(wt,val,N,W):

    #base condition for the recursive solution
    # if N==0 or W ==0:
    #     return 0
    if N == 1:
        return (W//wt[N-1])*val[N-1]
        
    #if we are not considering this element even once
    noPick = 0 + knapsack_with_duplicates_recursive(wt,val,N-1,W)
    pick = float('-inf')
    if wt[N-1]<= W:
        pick = val[N-1] + knapsack_with_duplicates_recursive(wt,val,N,W-wt[N-1])
    
    return max(pick,noPick)


N = 4
W = 8
val = [6, 1, 7, 7]
wt = [1, 3, 4, 5]

print('recursive solution',knapsack_with_duplicates_recursive(wt,val,N,W))

#top down approach
def knapsack_with_duplicates(wt,val,N,W):
    mtx = [[0 for i in range(W+1)] for j in range(N+1)]

    for i in range(N+1):
        for j in range(W+1):
            if i==0 or j ==0:
                mtx[i][j] = 0
            elif wt[i-1] <= j:
                mtx[i][j] = max((val[i-1] + mtx[i][j-wt[i-1]]) , mtx[i-1][j])
            else:
                mtx[i][j] = mtx[i-1][j]
    
    return mtx[N][W]


N = 4
W = 8
val = [6, 1, 7, 7]
wt = [1, 3, 4, 5]

print("Tabulation",knapsack_with_duplicates(wt,val,N,W))


