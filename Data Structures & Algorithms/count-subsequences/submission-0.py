class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def dfs(current, i):
            if current == t:
                return 1
            
            if i >= len(s):
                return 0
            
            return dfs(current + s[i], i + 1) + dfs(current, i + 1)

        return dfs("", 0)