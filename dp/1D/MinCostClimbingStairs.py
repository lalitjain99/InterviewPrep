"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either
climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999

"""
#Approach1: Recursion
#Time complexity : 2**N (At every step we have two possibilities either to take 1 step or 2 step )
#Space Complexity: N (Auxiliary stack Space for recursion since we can take 1 step n times so it will be n)
def minCost(cost,idx):
    if idx == 0 or idx == 1:
        return cost[idx]

    oneStep = cost[idx] + minCost(cost,idx-1)
    twoStep = cost[idx] + minCost(cost,idx-2)

    return min(oneStep,twoStep)


cost = [1,100,1,1,1,100,1,1,100,1]
n = len(cost)
print("Recursion: Minimum cost of climbing Stairs", min(minCost(cost,n-1),minCost(cost,n-2)))


#Approach 2: Recursion with memoization
#Time complexity: O(N) (since we are solving every step problem only once so it becomes N)
#Space Complexity: O(N + N) ( Auxiliary stack space for recursion + N space for storing dp values)
def minCost_memo(cost,idx):

    if idx == 0 or idx == 1:
        return cost[idx]
    if dp[idx] != -1:
        return dp[idx]
    oneStep = cost[idx] + minCost_memo(cost,idx-1)
    twoStep = cost[idx] + minCost_memo(cost,idx-2)
    dp[idx] = min(oneStep,twoStep)
    return dp[idx]

cost = [1,100,1,1,1,100,1,1,100,1]
n = len(cost)
dp = [-1]*n
print("Recursion with memoization: Minimum cost of climbing Stairs", min(minCost_memo(cost,n-1),minCost_memo(cost,n-2)))
 
#Approach 3: Tabulation
#Time complexity: O(N)
#Space Complexity: O(N)
def minCost_tab(cost):
    n = len(cost)
    dp = [-1]*n

    for i in range(n):
        if i < 2:
            dp[i] = cost[i]
        else:
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

    return min(dp[n-1],dp[n-2])

cost = [1,100,1,1,1,100,1,1,100,1]
print("Tabulation: Minimum cost of climbing Stairs",minCost_tab(cost))
