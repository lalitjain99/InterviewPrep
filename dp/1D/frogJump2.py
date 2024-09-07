"""
There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi.

There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:

If the frog is currently on Stone i, jump to one of the following: Stone i+1,i+2,…,i+K. Here, a cost of ∣hi −hj∣ is incurred, where 
j is the stone to land on. Find the minimum possible total cost incurred before the frog reaches Stone N.

Constraints
All values in input are integers.
2≤N≤10*5
1≤K≤100
1≤hi≤10*4

Sample Input 1
5 3
10 30 40 50 20
Sample Output 1
30
If we follow the path 1 → 2 → 5, the total cost incurred would be 
10 -30 + 30 - 20 =30.

Sample Input 2 
3 1
10 20 10
Sample Output 2
20
If we follow the path 
1 → 2 → 3, the total cost incurred would be 
10-20 + 20-10 =20.

Sample Input 3
2 100
10 10
Sample Output 3
0
If we follow the path 1 → 2, the total cost incurred would be 
10 - 10 =0.

Sample Input 4
10 4
40 10 20 70 80 10 20 70 80 60
Sample Output 4

40
If we follow the path 1 → 4 → 8 → 10, the total cost incurred would be 40 - 70 + 70 - 70 + 70 -60 = 40.

"""
#Approach 1: recursion

def frogJump_with_k_recur(heights,n):
    # Base case: If the frog is at the last floor, no energy is exhausted
    if n == 0:
        return 0
    min_step = float('inf')
    for i in range(1,k+1):
        # 1 step case: Frog bounces 1 floor, and energy is exhausted from the previous floor to the current floor
        if n-i>=0:
            jump = frogJump_with_k_recur(heights,n-i) + abs(heights[n]-heights[n-i])
            min_step = min(min_step,jump)

    # The minimum of the two computed values is the answer
    return min_step



n,k = 5,3
heights = [10, 30, 40, 50, 20]
print("minimum energy spent with {k} jumps using recursive solution".format(k=k),frogJump_with_k_recur(heights,n-1))

#Approach 2: recursion with memoization
dp= [-1]*n
def frogJump_with_k_memo(heights,n):

    #base case : If the frog is at the last floor , no energy is exhasted
    if n == 0:
        return 0
    #check if subproblem is already solved
    if dp[n] != -1:
        return dp[n]
    
    min_loss = float("inf")
    for i in range(1,k+1):

        if n-i>=0:
            loss = frogJump_with_k_memo(heights,n-i) + abs(heights[n] - heights[n-i])

            min_loss = min(loss,min_loss)
            dp[n] = min_loss

    return dp[n-1]

n,k = 5,3
heights = [10, 30, 40, 50, 20]
print("minimum energy spent with {k} jumps using recursive and memoization".format(k=k),frogJump_with_k_memo(heights,n-1))


def frogJump_tab(stones,n):
    dp = [-1]*(n)
    dp[0] = 0
    for i in range(1,n):
        min_loss = float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                loss = dp[i-j] + abs(stones[i]-stones[i-j])
                min_loss = min(loss,min_loss)
        dp[i] = min_loss
    return dp[n-1]

n,k = 5,3
stones = [10, 30, 40, 50, 20]
print("minimum energy spent with {k} jumps using tabulation".format(k=k),frogJump_tab(stones,n))