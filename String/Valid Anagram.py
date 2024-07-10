"""
Problem Statement : Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
"""
# Solution 1: Using HashMap
def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] = hashMap[s[i]] + 1
            else:
                hashMap[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in hashMap:
                hashMap[t[j]] = hashMap[t[j]] - 1
            else:
                hashMap[t[j]] = 1
        
        for k,v in hashMap.items():
            if v != 0:
                return False
        return True
