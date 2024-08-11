"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 
"""
people = [3,5,3,4]
limit = 5

def numRescueBoats( people: list[int], limit: int) -> int:
    people.sort()
    numberOfBoat = 0
    left = 0
    right = len(people) -1
    while left <= right:
        numberOfBoat +=1
        if people[left] + people [right] <= limit:
            left +=1
        
        right -= 1

    return numberOfBoat

print(numRescueBoats(people,limit))
