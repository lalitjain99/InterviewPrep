"""
Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.


Example 1:

Input: str = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings 
are "a", "babbbab", "b", "ababa".
Example 2:

Input: str = "aaabba"
Output: 1
Explaination: The substrings after 1
partitioning are "aa" and "abba".

"""

# Approach: This approach is similar to that of Matrix Chain Multiplication problem.

# In this approach, we recursively evaluate the following conditions:

# If the current string is a palindrome, then we simply return true, as Palindrome Partitioning is possible.
# Else, like the Matrix Chain Multiplication problem,
# we try making cuts at all possible places,
# recursively calculate the cost for each cut
# return the minimum value.
maxint=int(1e9+7)
def is_palindrome(arr,i,j):

        if i == j:
            return True
        
        if i>j :
            return True
        
        while i<j:
            if arr[i] != arr[j]:
                return False
            i +=1
            j -= 1

        return True

def palindromePartioning(arr,i,j):
  
    if i>=j or is_palindrome(arr,i,j):
        return 0
    
    _min = maxint

    for k in range(i,j):
        temp = palindromePartioning(arr,i,k) + palindromePartioning(arr,k+1,j) + 1

        _min = min(temp,_min)

    return _min


arr = "ababbbabbababa"
print("palindromePartioning with recursion",palindromePartioning(arr,0,len(arr)-1))
    

#Approach 2: recursive with memoization

arr = "ababbbabbababa"
i = 0
j = len(arr)-1
mtx = [[-1 for m in range(j+1)] for n in range(j+1)]

def palindromePartioningMemo(arr,i,j):

    #check for boundary conditions
    if i >= j or is_palindrome(arr,i,j):
        return 0
    
    if mtx[i][j] != -1:
        return mtx[i][j]
    
    _min = maxint

    for k in range(i,j):
        if mtx[i][k] != -1:
            left = mtx[i][k]
        else:
            left = palindromePartioningMemo(arr,i,k)
            mtx[i][k] = left
        
        if mtx[k+1][j] != -1:
            right = mtx[k+1][j]
        else:
            right = palindromePartioningMemo(arr,k+1,j)
            mtx[k+1][j] = right
        temp = 1 + left + right
        _min = min(temp,_min)

    mtx[i][j] = _min

    return mtx[i][j]

print("palindrome partition with recursion and memoization",palindromePartioningMemo(arr,i,j))

    

     