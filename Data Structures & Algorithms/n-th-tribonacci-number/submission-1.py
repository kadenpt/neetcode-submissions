class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        # Tn = Tn-3 + Tn-2 + Tn-1
        memo = [-1] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        def dfs(i):
            if memo[i] != -1:
                return memo[i]

            memo[i] = dfs(i - 3) + dfs(i - 2) + dfs(i - 1)
            return memo[i]
        
        return dfs(n)