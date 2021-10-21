'''
Problem Statement:
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

 class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict = Counter(ransomNote)
        for letter in ransomNote:
                if letter in magazine:
                    #letters cannot be reused, so the number of occurences of the letter to be matched has to be substracted
                    noteDict[letter]-= 1
                    #only remove that particular instance of the letter since lettes cannot be reused
                    magazine =  magazine.replace(letter,"",1)
        
        for key, freq in noteDict.items():
            #freq gives the number of occurences of the letters in the ransomNote which were not matched to magazine
            if freq > 0:
                return False
        
        return True

#Solution 2:
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteDict=Counter(ransomNote)
        magDict=Counter(magazine)
        for key,freq in noteDict.items():
            if(noteDict[key]<=magDict[key]):
                continue
            else:
                return False
        return True