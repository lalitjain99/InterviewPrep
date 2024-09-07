"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
# Climbing Stairs using Recursion:
# We can easily find the recursive nature in the above problem. The person can reach nth stair from either (n-1)th stair or from (n-2)th stair. Hence, for each stair n, we try to find out the number of ways to reach n-1th stair and n-2th stair and add them to give the answer for the nth stair. Therefore the Recurrence relation for such an approach comes out to be : 
# ways(n) = ways(n-1) + ways(n-2)

# time and space optimized solution
def climbingStair(n):
    step1,step2 = 1,1

    for i in range(n):
        temp = step1 + step2
        step1 = step2
        step2 = temp
    
    return step1

n=5
print("Number of ways to climb {n} steps using space optimized approach".format(n=n),climbingStair(n))

#approach 2: using dp tabulation bottom up
def climbingStair_dp(n):
    dp= [-1]*n
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]
n=5
print("Number of ways to climb {n} steps using tabulation".format(n=n),climbingStair_dp(n))

#approach 3 using recursion

def climbingStair_recur(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbingStair_recur(n-1) + climbingStair_recur(n-2)

n=5
print("number of way to climb {n} steps using recursion".format(n=n),climbingStair_recur(n))

#Approach 4 : Recursion with memoization



def climbingStair_memo(n):
    if n == 0:
        return 0 
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    else:
        dp[0] = 1
        dp[1] = 2
        
        dp[n] = climbingStair_memo(n-1) + climbingStair_memo(n-2)
        return dp[n-1]
n=5
#initialize a array to store subproblems
dp = [0]*n
print("number of way to climb {n} steps using recursion with memoization".format(n=n),climbingStair_recur(n))

