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
# W - Capacity of the bag
# wt - Weight array
# val - Value array
# n - Number of items 

# 1st Approach - recursive

# A simple solution is to consider all subsets of items and calculate the total weight and profit of all subsets. Consider the only subsets whose total weight is smaller than W. From all such subsets, pick the subset with maximum profit.

# Optimal Substructure: To consider all subsets of items, there can be two cases for every item. 

# Case 1: The item is included in the optimal subset.
# Case 2: The item is not included in the optimal set.

# Follow the below steps to solve the problem:

# The maximum value obtained from ‘N’ items is the max of the following two values. 

# Case 1 (include the Nth item): Value of the Nth item plus maximum value obtained by remaining N-1 items and remaining weight i.e. (W-weight of the Nth item).
# Case 2 (exclude the Nth item): Maximum value obtained by N-1 items and W weight.
# If the weight of the ‘Nth‘ item is greater than ‘W’, then the Nth item cannot be included and Case 2 is the only possibility.

def knapSack(W, wt, val, n):
    #base condition
    #if there is no item or bag capacity is null, then no value can be added hence return 0
    if n == 0 or W == 0:
        return 0
    
    #recursion
    # in order to add any item in the bag first condition is that its weight should be either less or equal to the bag capacity
    # once it satisfy the weight criteria we then have to make a decision whether to include a given weight or reject it
    if wt[n-1]<= W:
        max_value = max((val[n-1] + knapSack(W-wt[n-1],wt,val,n-1)), knapSack(W,wt,val,n-1))
    else:
        max_value = knapSack(W,wt,val,n-1)

    return max_value

N = 3
W = 3
values = [1,2,3]
weight = [4,5,6]

print("recursive approach", knapSack(W,wt=weight,val=values,n=N))

# 2nd approach recursive + memoization
# here important thing is to find the size of the matrix

def knapSack_with_memo(W, wt, val, n):
    #base condition
    tab = [[-1 for i in range(2000)] for j in range(2000)]
    if n == 0 or W == 0:
        return 0
    
    if tab[n-1][W] != -1:
        return tab[n-1][W]
    
    if wt[n-1]<= W:
        tab[n-1][W] = max((val[n-1] + knapSack_with_memo(W-wt[n-1],wt,val,n-1)), knapSack_with_memo(W,wt,val,n-1))
        return tab[n-1][W]

    else:
        tab[n-1][W] = knapSack_with_memo(W,wt,val,n-1)

    return tab[n-1][W]
N = 3
W = 3
values = [1,2,3]
weight = [4,5,6]

print("recursive approach", knapSack_with_memo(W,wt=weight,val=values,n=N))


#3rd approach top down approach

def knapSack_top_down(W, wt, val, n):
    #initialize a matrix with n+1 and W+1 size 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


N = 3
W = 50
values = [60, 100, 120]
weight = [10, 20, 30]

print('top down approach',knapSack_top_down(W,wt=weight,val=values,n=N))
    

