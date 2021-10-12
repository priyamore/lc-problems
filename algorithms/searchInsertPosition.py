'''
Problem Statement: Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

# Solution 1:

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1,
        while left <= right:
            mid = left + ((right -left) // 2) #to avoid the integer overflow issue
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if mid == 0: # in case its lesser than the first number, it will be added at the first position i.e 0th
                    return mid
                elif target > nums[mid-1]: # less than mid but greater than its previous number
                    return mid
                right = mid - 1
            elif target > nums[mid]:
                if mid == len(nums) - 1: # in case its greater the last number, the target will be added at the end
                    return mid+1
                elif target < nums[mid+1]: # greater than mid but less than its next number
                    return mid+1
                left = mid +1  