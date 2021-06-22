class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        max_profit, min_price = 0, float('inf')
        for i in prices:
            min_price = min(min_price, i)
            profit = i - min_price
            max_profit = max(max_profit, profit)
        return max_profit
        """

        maxsofar = 0
        min_price = float('inf')
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                maxsofar = max(maxsofar, i - min_price)
        return maxsofar