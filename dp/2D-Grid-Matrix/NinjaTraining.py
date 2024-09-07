"""
Ninja is planing this N days-long training schedule. Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). Each activity has some merit points on each day. As Ninja has to improve all his skills, he can't do the same activity in two consecutive days. Can you help Ninja find out the maximum merit points Ninja can earn?

You are given a 2D array of size N*3 POINTS with the points corresponding to each day and activity. Your task is to calculate the maximum number of merit points that Ninja can earn.

For Example
If the given POINTS array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
"""
#Approach 1: Recursion
#Time Complexity: 3*2**(N-1)--> 2**(N-1)
#Space Complexity: O(N)
def NinjaTraining(points,day,lastActivity):
    #check for boundary condition
    if day  == 0:
        point0 = 0
        for activity in range(3):
            if activity != lastActivity:
                point0 = max(point0,points[day][activity])
        return point0
    maxPoints = 0
    for activity in range(3):
        if activity != lastActivity:
            point = points[day][activity]  + NinjaTraining(points,day-1,lastActivity=activity)
            maxPoints = max(point,maxPoints)
    return maxPoints



points = [[1,2,5], [3 ,1 ,4] ,[3,7,9] ]     

print("Recursion: Maximum training points will be",NinjaTraining(points,2,3))


#Approach 2: Recursion with Memoization   
#Time Complexity: O(3*(N-1) + 3)-->O(N)     size of dp * function execution  --> O(N*M)*(3+3) --> where N is number of days , M is number of activities
#Space Complexity: O(N) + O(N*3) --> O(N)
def NinjaTraining_Memo(points,day,lastActivity):
    if day  == 0:
        point0 = 0
        for activity in range(3):
            if activity != lastActivity:
                point0 = max(point0,points[day][activity])
        return point0
    if dp[day][lastActivity] != 0:
        return dp[day][lastActivity]
    maxPoints = 0
    for activity in range(3):
        if activity != lastActivity:
            point = points[day][activity]  + NinjaTraining_Memo(points,day-1,lastActivity=activity)
            maxPoints = max(point,maxPoints)
            dp[day][lastActivity] = maxPoints
    return dp[day][lastActivity]

points = [[1,2,5], [3 ,1 ,1] ,[3,3,3] ] 
days = len(points)
dp = [[0 for _ in range(4)] for _ in range(days) ]
print("Recursion with memoization: Maximum number of training points will be ",NinjaTraining_Memo(points,days-1,3))


#Approach 3: Tabulation

def NinjaTraining_tab(points):
    days  = len(points)
    
    if days == 1:
        return max(points[0][2],max(points[0][0],points[0][1]))
    
    dp = [[0 for _ in range(3)] for _ in range(days)]

    dp[0] = points[0]

    trainingPoints = float("-inf")
    for day in range(1,days):
        for activity in range(3):
            if activity == 0:
                dp[day][activity] = points[day][activity] + max(dp[day-1][activity+1],dp[day-1][activity+2])
            elif activity == 1:
                dp[day][activity] = points[day][activity] + max(dp[day-1][activity-1],dp[day-1][activity+1])
            elif activity == 2:
                dp[day][activity] = points[day][activity] + max(dp[day-1][activity-1],dp[day-1][activity-2])

    for activity in range(3):
        trainingPoints = max(trainingPoints,dp[days-1][activity])

    return trainingPoints

points = [[1,2,5], [3 ,1 ,1] ,[3,3,3]] 
print("Tabulation: Maximum number of training points will be ",NinjaTraining_tab(points))