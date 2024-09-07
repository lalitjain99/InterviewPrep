"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 
"""
#Approach 1: Recursion
def maxProfit(prices,idx,buy,fee):
    #boundary condition
    if idx == len(prices):
        return 0
    
    if buy:
        buying = -prices[idx] + maxProfit(prices,idx+1,0,fee)
        notBuying = maxProfit(prices,idx+1,1,fee)
        profit = max(buying,notBuying)
        return profit

    else:
        selling = prices[idx] - fee + maxProfit(prices,idx+1,1,fee)
        notSelling = maxProfit(prices,idx+1,0,fee)
        profit = max(selling,notSelling)
        return profit
    
prices = [1,3,7,5,10,3]
fee = 3
print("Recursion: max profit when reach transaction is charged with fee {a} is".format(a=fee),maxProfit(prices,0,1,fee))

#Approach 2: Recursion with memoization

def maxProfit_memo(prices,idx,buy,fee):
    #boundary condition
    if idx == len(prices):
        return 0
    if dp[idx][buy] != -1:
        return dp[idx][buy]
    if buy:
        buying = -prices[idx] + maxProfit_memo(prices,idx+1,0,fee)
        notBuying = maxProfit_memo(prices,idx+1,1,fee)
        dp[idx][buy] = max(buying,notBuying)
        return dp[idx][buy]

    else:
        selling = prices[idx] - fee + maxProfit_memo(prices,idx+1,1,fee)
        notSelling = maxProfit_memo(prices,idx+1,0,fee)
        dp[idx][buy] = max(selling,notSelling)
        return dp[idx][buy]
    
prices = [1,3,7,5,10,3]
fee = 3
dp = [[-1 for _ in range(2)] for _ in range(len(prices)+1)]
print("Recursion with memoization: max profit when reach transaction is charged with fee {a} is".format(a=fee),maxProfit_memo(prices,0,1,fee))

#Approach 3: Tabulation

def maxProfit_tab(prices,fee):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n+1)]

    #base condition
    dp[n][0] = 0
    dp[n][1] = 0


    for i in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                dp[i][buy] = max((-prices[i] + dp[i+1][0]),dp[i+1][1])
            else:
                dp[i][buy] = max((prices[i]-fee+dp[i+1][1]),dp[i+1][0])

    return dp[0][1]

prices = [1,3,7,5,10,3]
fee = 3
print("Recursion: max profit when reach transaction is charged with fee {a} is".format(a=fee),maxProfit_tab(prices,fee))