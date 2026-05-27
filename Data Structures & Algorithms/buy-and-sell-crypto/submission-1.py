class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minor = float('inf')
        profit = 0

        for price in prices:

            minor = min(minor, price)

            profit = max(profit, price - minor)

        return profit