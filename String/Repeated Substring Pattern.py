"""
Problem Statement: Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""

# Solution
def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
       
        n = len(s)
        # Check possible lengths of substrings
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                # Extract the substring of current length
                substring = s[:length]
                # Check if repeating this substring forms the original string
                if substring * (n // length) == s:
                    return True
        return False


        
        
            
        
