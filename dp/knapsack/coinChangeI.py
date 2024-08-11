"""
Given an integer array of coins[ ] of size N representing different types of denominations and an integer sum, the task is to count all combinations of coins to make a given value sum.  

Note: Assume that you have an infinite supply of each type of coin. 

Examples: 

Input: sum = 4, coins[] = {1,2,3}, 
Output: 4
Explanation: there are four solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}. 

Input: sum = 10, coins[] = {2, 5, 3, 6}
Output: 5
Explanation: There are five solutions: 
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.

"""

def countCoinSet(coins:list, amount: int) -> int:
    N = len(coins)
    dp = [[0 for i in range(amount+1)] for j in range(N+1)]

    #boundary conditions
    #if sum is zero than we can array return a empty array so its true for any number of from coins 
    for i in range(0,N+1):
        dp[i][0] = 1
    
    #if sum is greater than zero and number of coins is zero than we can never have any such set which can be equal to given sum
    for i in range(1,amount+1):
        dp[0][i] = 0

    for i in range(1,N+1):
        for j in range(0,amount+1):
            if coins[i-1]<= j:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N][amount]

sum = 10
coins = [2, 5, 3, 6]

print(countCoinSet(coins=coins,amount=sum))