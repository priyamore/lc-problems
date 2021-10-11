'''
Given an integer array nums, find the contiguous(consecutive) 
subarray (containing at least one number) 
which has the largest sum and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largestSum, currSum = max(nums), 0
        for num in nums:
            currSum = currSum + num
            if currSum >= largestSum:
                largestSum = currSum
            ''' if currentSum is negative then dont add that, 
             instead add 0(which is greater than all the negative numbers) '''
            if currSum < 0:
                currSum = 0
        return largestSum