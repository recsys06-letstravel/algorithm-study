# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # brute forec time limit exceeded

        # sub = -1
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         sub = max(sub, prices[j] - prices[i])
        #
        # if sub < 0:
        #     return 0
        #
        # return sub

        # 최소 최대 와리가리.
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit