class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        
        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0

            if total == amount:
                return 1

            if memo[i][total] != -1:
                return memo[i][total]
            
            memo[i][total] = (dfs(i, total + coins[i]) + dfs(i + 1, total))
            return memo[i][total]

        return dfs(0, 0)