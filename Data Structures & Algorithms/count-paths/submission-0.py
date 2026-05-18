class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        def dfs(i, j):
            if (i > n - 1 or j > m - 1):
                return 0
            
            if i == n - 1 and j == m - 1:
                return 1
            
            return (dfs(i + 1, j) +
                    dfs(i, j + 1))

        
        return dfs(0, 0)