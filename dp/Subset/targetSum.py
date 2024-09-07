"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""

#Approach 1: Recursion

def findTargetSumWays(nums,n,target):
    if n == 0:
        return 1 if (nums[n] == target) or (-nums[n] == target) else 0
    
    minusSign = findTargetSumWays(nums,n-1,target+nums[n-1])
    plusSign = findTargetSumWays(nums,n-1,target-nums[n-1])

    return minusSign + plusSign

nums = [1]
n = 1
target = 1

print("Recursion: Number of ways to find target are",findTargetSumWays(nums,n-1,target))

#Approach 2: Recursion with memoization

def findTargetSumWays_memo(nums,n,target):
    if n == 1:
        return 1 if (nums[n-1] == target) or (-nums[n-1] == target) else 0
    print("n",n)
    if dp[n][target] != -1:
        return dp[n][target]
    minusSign = findTargetSumWays_memo(nums,n-1,target+nums[n-1])
    plusSign = findTargetSumWays_memo(nums,n-1,target-nums[n-1])
    dp[n][target] = minusSign + plusSign
    return dp[n][target]

nums = [1,1,1,1,1]
n = 5
target = 3
dp = [[-1]*(sum(nums)+1) for _ in range(n+1)]
# print(dp)
print("Recursion with memoization: Number of ways to find target are",findTargetSumWays_memo(nums,n,target))

#Approach 3: tabulation
def findTargetSumWays_tab(nums,target):
        n = len(nums)
        #check if only single digit is given
        if n == 1:
            return 1 if (nums[0] == target) or (-nums[0] == target) else 0

        total = sum(nums)  
        #check if sum of total array sum and difference i.e. target is even
        if (total+target)%2 != 0:
            return 0
        # this condition checks if difference is achievable or not considering any sign
        if total < abs(target):
            return 0

        targetSum = (total+ target)//2
    
        dp = [[0]*(targetSum +1) for _ in range((n+1))]
        #base condition 
        dp[0][0] = 1
        
        for i in range(1,n+1):
            for j in range(0,targetSum+1):
                dp[i][j] = dp[i-1][j]
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                    
                    dp[i][j] %=10**9 +7
        
        return dp[n][targetSum]

nums = [1,1,1,1,1]
target = 3

print("Tabulation: Number of ways to find target are",findTargetSumWays_tab(nums,target))