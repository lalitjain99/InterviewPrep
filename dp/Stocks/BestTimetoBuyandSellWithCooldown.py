"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

#Approach 1: Recursion 

def maxProfit(prices,idx,buy):
    if idx >= len(prices):
        return 0

    if buy:
        buying = -prices[idx] + maxProfit(prices,idx+1,0)
        notBuying = 0 + maxProfit(prices,idx+1,1)
        profit = max(buying,notBuying)
        return profit
    else:
        selling = prices[idx] + maxProfit(prices,idx+2,1)
        notSelling = 0 + maxProfit(prices,idx+1,0)
        profit = max(selling,notSelling)
        return profit

prices = [1,2,3,0,2]
print("Recursion: max profit when you have a cooldown is",maxProfit(prices,0,1))