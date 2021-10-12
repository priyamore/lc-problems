'''
Problem Statement:
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity. 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
'''
#Solution 1 - Iterative

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left , right = 0, len(nums) - 1,
        while left <= right:
            mid = left + ((right -left) // 2) #to avoid the integer overflow issue
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid +1
        return -1

##Solution 2 - Rescursive

class Solution:
    #recursive function
    def binarySearch(self, nums: List[int], left: int, right: int, target: int):
        if left <= right:
            mid = left + ((right - left) // 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return self.binarySearch(nums, left, mid - 1, target)
            elif target > nums[mid]:
                return self.binarySearch(nums, mid + 1, right, target)
        else:
            return -1
        
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)