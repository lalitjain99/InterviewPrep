"""
You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.

"""

def countAsterisks(s: str) -> int:
    bar_even, star = True, 0
    for c in s:
        if c == '|':
            bar_even = not bar_even
        elif c == '*' and bar_even:
            star += 1   
    return star


s = "l|*e*et|c**o|*de|"

print(countAsterisks(s))