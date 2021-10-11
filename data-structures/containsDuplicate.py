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