"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""

#Approach 1 : Recursion

def maxProfit(prices,idx,buy):
    if idx == len(prices):
        return 0
    
    #if buying is allowed , then we have 2 choice either we want to buy or not to BoxLayout:
    if buy:
        #if we are buying than , that much money will be deducted from the profit hence we use -ve sign and moving to the next day setting buying is not allowed (i.e. buy = 0)
        buying = - prices[idx] + maxProfit(prices,idx+1,0)
        #if we decide not buy, then no change in the profit and move the next day with buying still allowed (i.e. buy = 1)
        notBuying = 0 + maxProfit(prices,idx+1,1)
        #we take the maximum of these two conditions
        profit = max(buying,notBuying)
    # on the selling part again we have 2 choices whether to sell or not to sell 
    else:
        # we are selling the stock, then that amount will be added to the profit and move to the next day with buying allowed(i.e. buy = 1)
        sell = prices[idx] + maxProfit(prices,idx+1,1)
        #we are not selling the stock, then no change in profit and move to next dat with buying not allowed (i.e. buy = 0)
        notSell = 0 + maxProfit(prices,idx+1,0)

        profit = max(sell,notSell)

    return profit

prices = [7,1,5,3,6,4]
print("Recursion: maximum profit is",maxProfit(prices,0,1))


#Approach 2 : Recursion with memoization

def maxProfit_memo(prices,idx,buy):

    if idx == len(prices):
        return 0
    # print("idx",idx)
    if dp[idx][buy] != -1:
        return dp[idx][buy]
    
    if buy:
        buying = -prices[idx] + maxProfit_memo(prices,idx+1,0)
        notBuying  = 0 + maxProfit_memo(prices,idx+1,1)
        dp[idx][buy] = max(buying,notBuying)
        return dp[idx][buy]

    else:
        selling = prices[idx] + maxProfit_memo(prices,idx+1,1)
        notSelling = 0 + maxProfit_memo(prices,idx+1,0)
        dp[idx][buy] = max(selling,notSelling)
        return dp[len(prices)-1][buy]

prices = [7,1,5,3,6,4]
dp = [[-1 for _ in range(2)] for _ in range((len(prices)+1))]
print("Recursion with memoization: maximum profit is ",maxProfit_memo(prices,0,1))

# intuitive approach
def maxProfit_intuitive(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            profit += prices[i]-prices[i-1]

    return profit
prices = [7,1,5,3,6,4]
print("Intuitive approach: max profit  is",maxProfit_intuitive(prices))

#tabulation

def maxProfit_tab(prices):
    n = len(prices)
    dp = [[-1 for i in range(2)] for _ in range(n+1)]

    dp[n][0] = 0
    dp[n][1] = 0


    for i in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                dp[i][buy] = max((-prices[i]+ dp[i+1][0]),dp[i+1][1])
            else:
                dp[i][buy] = max((prices[i] + dp[i+1][1]),dp[i+1][0])

    return dp[0][1]

prices = [7,1,5,3,6,4]
print("Tabulation: maximum profit is",maxProfit_tab(prices))