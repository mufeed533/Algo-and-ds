"https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/"

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0,0

        max_profit = 0

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max_profit
