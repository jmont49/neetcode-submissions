class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        least = prices[0]

        profit = 0

        for price in prices:
            least = min(price, least)

            if price > least:
                profit = max(profit, price - least)

        return profit

        