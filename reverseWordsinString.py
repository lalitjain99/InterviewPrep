"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

def reverseWords(s: str) -> str:
    input_list = list(s.split(" "))
    
    output_list = []
    for word in input_list:
        output_list.append(word[::-1])

    out_s = " ".join(output_list)

    return out_s


s = "Let's take LeetCode contest"

print(reverseWords(s))