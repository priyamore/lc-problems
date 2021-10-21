'''
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example:
i/p: [5,2,6,3,7,1]
o/p: 5
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, profit = prices[0], 0
        #maximize the profit and minimize the buying price
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            profit = max(profit, prices[i] - minPrice)
        return profit