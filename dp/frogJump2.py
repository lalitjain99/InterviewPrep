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
print("minimum energy spent with k jumps",frogJump_with_k_recur(heights,n-1))