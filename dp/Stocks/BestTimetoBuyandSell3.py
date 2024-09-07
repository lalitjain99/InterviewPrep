"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105

"""

#Approach 1: Recursion 

def maxProfit(prices,idx,buy,txn):
    if txn == 0:
        return 0
    
    if idx == len(prices):
        return 0

    if buy:
        buying = -prices[idx] + maxProfit(prices,idx+1,0,txn)
        notBuying = 0 + maxProfit(prices,idx+1,1,txn)
        profit = max(buying,notBuying)
        return profit
    else:
        selling = prices[idx] + maxProfit(prices,idx+1,1,txn-1)
        notSelling = 0 + maxProfit(prices,idx+1,0,txn)
        profit = max(selling,notSelling)
        return profit

prices = [3,3,5,0,0,3,1,4]
print("Recursion: max profit when at max only 2 txn are allowed is",maxProfit(prices,0,1,2))

#Approach 2: Recursion with Memoization
def maxProfit_memo(prices,idx,buy,txn):
    if txn == 0:
        return 0
    
    if idx == len(prices):
        return 0

    if dp[idx][buy][txn] != -1:
        return dp[idx][buy][txn]
    if buy:
        buying = -prices[idx] + maxProfit_memo(prices,idx+1,0,txn)
        notBuying = 0 + maxProfit_memo(prices,idx+1,1,txn)
        dp[idx][buy][txn] = max(buying,notBuying)
        return dp[idx][buy][txn]

    else:
        selling = prices[idx] + maxProfit_memo(prices,idx+1,1,txn-1)
        notSelling = 0 + maxProfit_memo(prices,idx+1,0,txn)
        dp[idx][buy][txn] = max(selling,notSelling)
        return dp[idx][buy][txn]

prices = [3,3,5,0,0,3,1,4]
dp = [[[-1]*3]*(2)]*(len(prices))
print("Recursion with memoization: max profit when at max only 2 txn are allowed is",maxProfit_memo(prices,0,1,2))
        

#Approach 3: Tabulation

def maxProfit_tab(prices,txns):
    n = len(prices)
    dp = [[[0] * (txns + 1) for _ in range(2)] for _ in range(n + 1)]
    
    #base condition 1
    #handling if no more transaction can be made
    for i in range(0,n):
        for j in range(2):
            dp[i][j][0] = 0
    
    
    # base condition 2
    # if number of days is out of range
    for i in range(2):
        for j in range(txns+1):
            dp[n][i][j] = 0

    for i in range(n-1,-1,-1):
        for buy in range(2):
            for txn in range(1,txns+1):
                if buy:
                    dp[i][buy][txn] = max((-prices[i] + dp[i+1][0][txn]),dp[i+1][1][txn])
                else:
                    dp[i][buy][txn] = max((prices[i] + dp[i+1][1][txn-1]),dp[i+1][0][txn])

    return dp[0][1][txns]

prices = [3,3,5,0,0,3,1,4]
print("Tabulation: max profit when at max only 2 txn are allowed is",maxProfit_tab(prices,2))