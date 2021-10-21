'''
Problem Statemnet:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

#Solution 1:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        noteDict = Counter(s)
        #anagram is a rearrangement of another word so length must be same
        if len(s) == len(t):
            for letter in s:
                    if letter in t:
                        noteDict[letter]-= 1
                        t = t.replace(letter,"",1)
            for key, freq in noteDict.items():
                if freq > 0:
                    return False
            return True
        else:
            return False