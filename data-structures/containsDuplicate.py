'''
Problem Statement - Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
'''

#Solution 1 - using dict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create an empty dict
        numsDict = {}
        for num in nums:
            '''if the key for that particular num is made already 
            then the number already exists in the list, so return True'''
            if num in numsDict:
                return True
            #else add the entry for the new number
            else:
                numsDict[num] = 1
        #return false at the end of the list
        return False

#Solution 1 - using set(contains unique entries)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)