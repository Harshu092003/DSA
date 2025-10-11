class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            # Find the smallest price so far
            if price < min_price:
                min_price = price
            # Calculate profit if we sell today
            profit = price - min_price
            # Update max profit
            if profit > max_profit:
                max_profit = profit

        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
