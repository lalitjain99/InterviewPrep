"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""

#Approach 1: Recursion

def maxProfit(prices,idx,buy,txns):
    #boundary cases
    if txns == 0 or idx == len(prices):
        return 0
    
    if buy:
        buying = -prices[idx] + maxProfit(prices,idx+1,0,txns)
        notBuying = maxProfit(prices,idx+1,1,txns)
        profit = max(buying,notBuying)
        return profit
    else:
        selling = prices[idx] + maxProfit(prices,idx+1,1,txns-1)
        notSelling = maxProfit(prices,idx+1,0,txns)
        profit = max(selling,notSelling)
        return profit
    
prices = [3,2,6,5,0,3]
txns = 2
print("Recursion: maximum profit when {txns} are allowed is".format(txns=txns),maxProfit(prices,0,1,txns))


#
    