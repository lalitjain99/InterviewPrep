# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
    step1, step2 = 1,1
    for i in range(n-1):
        temp = step1
        step1 = step2 + step1
        step2 = temp

    return step1

n=5
print(climbStairs(n))