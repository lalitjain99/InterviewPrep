# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with the maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins that you can have.

def maxCoins(piles: list[int])-> int:
    piles.sort(reverse=True)
    coins = 0
    last = len(piles)//3
    for idx in range(1,len(piles)-last,2):
        coins = coins + piles[idx]
    return coins


piles = [9,8,7,6,5,1,2,3,4]
print(maxCoins(piles))

 