'''
Problem Statement:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
'''

#Solution 1

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = [[1]]
        for row in range(1, numRows):
            #first element of the row is always 1
            triangle.append([1])
            for i in range(1, row):
                triangle[row].append(triangle[row-1][i-1] + triangle[row-1][i])
            #last element of the row is always 1
            triangle[row].append(1)
        return triangle