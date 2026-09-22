class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for l in range(len(prices) - 1):
            r = l + 1
            current = prices[r]
            while r < len(prices):
                current = max(current, prices[r])
                r += 1
            res = max(current - prices[l], res)
        return res
