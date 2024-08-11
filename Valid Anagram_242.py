# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def char_freq_count(word):
    char_freq = {}
    for char in word:
        if char in char_freq:
            char_freq[char] +=1
        else:
            char_freq[char] = 1
    return char_freq

def valid_anagram(s: str,t: str):
    
    char_freq_s = char_freq_count(s)
    char_freq_t = char_freq_count(t)
    
    for char,count in char_freq_s.items():
        if char not in char_freq_t:
            return false
        elif char_freq_s[char] != char_freq_t[char]:
            return False
    
    return True
    
s = "anagram"
t = "nagaram"

print(valid_anagram(s,t))