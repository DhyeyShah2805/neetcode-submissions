class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        res = 0
        for i in prices:
            minPrice = min(minPrice, i)
            profit = i - minPrice
            res = max(res, profit)
        return res