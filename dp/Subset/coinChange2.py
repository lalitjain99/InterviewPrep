# Input: coins = [1,2,5], amount = 11

#time complexity : 2**n 
#space complexity : O(Amount)
def fn(coins, amount, n):
    # if amount == 0:
    #     return 0
    # if n==0:
    #     return float("inf")
    
    if n ==1 and  amount%coins[n-1] ==0:
        return amount//coins[n-1]
    elif n==1:
        return float("inf")
 

    noPick = 0 + fn(coins,amount,n-1) #0
    pick = float("inf")
    if coins[n-1]<=amount:
        pick = 1+ fn(coins,amount-coins[n-1],n)

    return min(pick,noPick)

coins = [2,5,10,1]
amount = 27
print(fn(coins,amount,len(coins)))

#Approach 2: Recursion with memoization

def 
#tab 
# def minCoins(coins,amount):
    