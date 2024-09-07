"""
Given a number n, print n-th Fibonacci Number. 

The Fibonacci numbers are the numbers in the following integer sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

Input  : n = 1

Output : 1

Input  : n = 9

Output : 34

Input  : n = 10

Output : 55
"""

# Approach 1:
# The Nth Fibonacci Number can be found using the recurrence relation shown above:

# if n = 0, then return 0. 
# If n = 1, then it should return 1. 
# For n > 1, it should return Fn-1 + Fn-2
import time

def fibonacci_rec(n):
    
    #base condition
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
n=2
start_time = time.time()
print("nth fibonacci number using recursion",fibonacci_rec(n))
end_time = time.time()
time_taken = end_time - start_time
print("time taken for recursion",time_taken)
#Approach 2

n = 2
dp = [-1]*(n+1)
def fibonacci_memo(n):
    #base condition
    if n==0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
        return dp[n]

start_time = time.time()
print("fibonacci number with memoization",fibonacci_memo(n))
end_time = time.time()
time_taken = end_time - start_time
print("time taken for recursion with memoization",time_taken)


#Approach 3 Tabulation (Bottom Up)

def fibonacci_tab(n):
    prev2 ,prev = 0,1
    if n==0:
        return prev2
    if n==1:
        return prev
    while n>=2:
        curr = prev + prev2
        prev2 = prev
        prev = curr
        n -= 1

    return prev

n = 6
start_time = time.time()
print("fibonacci with tabulation", fibonacci_tab(n))
end_time = time.time()
time_taken = end_time - start_time
print("time taken for recursion with tabulation",time_taken)