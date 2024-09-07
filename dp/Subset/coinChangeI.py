"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

"""
#Approach 1: Recursion
#time complexity : 2**n 
#space complexity : O(Amount)
def minCoins(coins, amount, n):
    # if amount == 0:
    #     return 0
    # if n==0:
    #     return float("inf")
    
    if n ==1 and  amount%coins[n-1] ==0:
        return amount//coins[n-1]
    elif n==1:
        return float("inf")
 

    noPick = 0 + minCoins(coins,amount,n-1) #0
    pick = float("inf")
    if coins[n-1]<=amount:
        pick = 1+ minCoins(coins,amount-coins[n-1],n)

    return min(pick,noPick)

coins = [2,5,10,1]
amount = 27
print("Recursion: minimum number of coins needed to make up the amount is ",minCoins(coins,amount,len(coins)))

#Approach 2 : Recursion with memoization

def minCoins_memo(coins,n,amount):

    if n ==1 and  amount%coins[n-1] ==0:
        return amount//coins[n-1]
    elif n==1:
        return float("inf")
    
    if dp[n][amount] != -1:
        return dp[n][amount]

    noPick = 0 + minCoins(coins,amount,n-1) #0
    pick = float("inf")
    if coins[n-1]<=amount:
        pick = 1+ minCoins(coins,amount-coins[n-1],n)

    return min(pick,noPick)

coins = [2,5,10,1]
amount = 27
n = len(coins)
dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
print("Recursion with memoization: minimum number of coins needed to make up the amount is ",minCoins(coins,amount,len(coins)))