"""
There are N stairs, numbered 1,2,…, N. For each i (1≤i≤N), the height of stair i is hi. There is a frog who is initially on stair 1. He will repeat the following action several times to reach stair N: If the frog is currently on stair I, jump to Stone i+1 or Stone i+2. Here, a cost of ∣hi −hj∣ is incurred, where j is the stone to land on.

Find the minimum possible total cost incurred before the frog reaches stair N.

Examples:

Input: n = 4, heights = [20, 30, 40, 20]
Output: 20
Explanation: The answer is 20, as the frog may jump from the first stair to the second i.e 1 step (|30-20| – 10 energy lost), and then from the second stair to the last i.e. 2 step (|30-20| = 10 energy lost), given the supplied HEIGHT array of (20,30,40,20). The total amount of energy lost is 20.

Input: n = 5, heights = [30, 20, 50, 10, 40]
Output: 30
Explanation: The answer is 30, as the frog may jump from the first stair to the third i.e. 2 step (|30-50| = 20 energy lost ), and then from the second stair to the last i.e. 2 step (|50-40| = 10 energy lost), given the supplied HEIGHT array of (30, 20, 50, 10, 40). The total amount of energy lost is 30.
"""
# Approach 1: Hopping Frog Using Recursion
# Start from the n and recursively call the function till 0. The minimum value can be computed using 2 options to perform for the frog i.e bounce 1 step or bounce 2 step.

# Follow the steps to Implement the Approach:

# Make a recursive function
# Compute for the base case
# Do the operations for the frog that is bouncing for 1 step or 2 steps i.e left or right (visualize a recursion tree for the call of left and right)
# Compute the min value from both the operations
# Return the min of both .


# def frogJump(heights,n):
#     #boundary conditions
#     dp = [0]*(n)
#     if n == 1:
#         return heights[n]
#     if n == 2:
#         return min(abs(heights[0]-heights[1]),heights[1])
#     else:
#         dp[0] = 0
#         dp[1] = min(abs(heights[0]-heights[1]),heights[1])
#         for i in range(2,n):
#             dp[i] = min((dp[i-1] + abs(heights[i]-heights[i-1])),(dp[i-2]+abs(heights[i]-heights[i-2])))
#             # print(dp)
#         return dp[n-1]

# n = 4
# heights = [20, 30, 40, 20]
# print("minimum cost ",frogJump(heights,n))


def frogJump_recur(heights,n):
    # Base case: If the frog is at the last floor, no energy is exhausted
    if n == 0:
        return 0
    
    # 1 step case: Frog bounces 1 floor, and energy is exhausted from the previous floor to the current floor
    # print("step1 execution begin")
    print("n before step1",n)
    # print("step1 before call",step1)
    step1 = frogJump_recur(heights,n-1) + abs(heights[n]-heights[n-1])
    print("step1 after call",step1)

    # Initialize right to a large value because we need to compute the minimum
    print("step2 execution")
    print("n before step2",n)
    step2 = float('inf')
    # Condition check if ind > 1 because it's not possible to jump 2 floors if the floor left is 1 or less
    if n>1:
        # 2step case: Frog bounces 2 floors, and energy is also exhausted from the two floors before the current floor
        print("step2 before call",step2)
        step2 = frogJump_recur(heights,n-2) + abs(heights[n]-heights[n-2])
        print("step2 after call",step2)
    # The minimum of the two computed values is the answer
    return min(step1,step2)
    
n = 4
heights = [20, 30, 40, 20]
print("minimum cost using recursion",frogJump_recur(heights,n-1))


#Approach 2: recursion with memoization

dp = [-1]*(n+1)
def frogJump_memo(heights,n):
    # Base case: If the frog is at the last floor, no energy is exhausted
    if n == 0:
        return 0
    
    if dp[n] != -1:
        return dp[n]
    # 1 step case: Frog bounces 1 floor, and energy is exhausted from the previous floor to the current floor
    step1 = frogJump_memo(heights,n-1) + abs(heights[n]-heights[n-1])

    # Initialize right to a large value because we need to compute the minimum
    step2 = float('inf')
    # Condition check if ind > 1 because it's not possible to jump 2 floors if the floor left is 1 or less
    if n>1:
        # 2step case: Frog bounces 2 floors, and energy is also exhausted from the two floors before the current floor
        step2 = frogJump_memo(heights,n-2) + abs(heights[n]-heights[n-2])
    # The minimum of the two computed values is the answer
    dp[n] = min(step1,step2)
    return dp[n]
    
n = 4
heights = [20, 30, 40, 20]
print("minimum cost using recursion with memoization",frogJump_memo(heights,n-1))

#Approach 3: Tabulation

def frogJump_tab(heights,n):
    dp = [-1]*(n)
    dp[0] = 0

    for i in range(1,n):
        oneStep = dp[i-1] + abs(heights[i]-heights[i-1])
        twoStep = float('inf')
        if i>1:
            twoStep = dp[i-2] + abs(heights[i]-heights[i-2])

        dp[i] = min(oneStep,twoStep)
    return dp[n-1]

n = 4
heights = [20, 30, 40, 20]
print("minimum cost using tabulation",frogJump_tab(heights,n))


#Approach 4 : space optimized 

def frogJump_tab(heights,n):
    prev = 0
    prev2 = 0

    for i in range(1,n):
        oneStep = prev + abs(heights[i]-heights[i-1])
        twoStep = float('inf')
        if i>1:
            twoStep = prev2 + abs(heights[i]-heights[i-2])

        curr = min(oneStep,twoStep)
        prev2 = prev
        prev = curr
    return prev

n = 4
heights = [20, 30, 40, 20]
print("minimum cost using tabulation and space optimization",frogJump_tab(heights,n))