"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

"""
digits = [1,9,9,9]
def oneplus(digits: list) -> list[int]:

    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i]+1
            return digits
        
    return [1] + digits

print(oneplus(digits))
