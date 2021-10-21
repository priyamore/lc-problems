'''
Problem Statement: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

#Solution 1:

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for sub in s:
            if s.count(sub) == 1:
                return s.index(sub)
        return -1

#Solution 2
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for sub, freq in Counter(s).items():
            if freq == 1:
                return s.find(sub)
        return -1