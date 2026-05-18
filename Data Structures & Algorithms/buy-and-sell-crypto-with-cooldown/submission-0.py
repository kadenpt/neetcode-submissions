class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i, owned):
            if i >= len(prices):
                return 0
            
            # always sell on last day
            if i == len(prices) - 1 and owned > 0:
                return prices[i] - prices[owned]
            
            # Scenario 1: Doesnt own a stock, can buy or wait
            if owned == -1:
                return max(dfs(i + 1, i),
                            dfs(i + 1, owned))

            # Scenario 2: Owns a stock, can either hold or sell
            if owned >= 0:
                return max(dfs(i + 1, owned),
                            prices[i] - prices[owned] + dfs(i + 2, -1))
            
            return 0

        return dfs(0, -1)

