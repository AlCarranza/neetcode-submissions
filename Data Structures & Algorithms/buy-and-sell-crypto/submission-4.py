class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = max_profit = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell]-prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        return max_profit