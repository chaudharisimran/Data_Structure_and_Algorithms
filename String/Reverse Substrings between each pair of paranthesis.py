"""
Problem Statement : You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
"""

## Solution 1:
def reverseParentheses(s):
    stack = []
    result = ""
    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.append(len(result))  # Store current result length
        elif s[i] == ')':
            start = stack.pop()
            result = result[:start] + result[start:][::-1]  # Reverse the substring
        else:
            result += s[i]
        i += 1
    
    return result

