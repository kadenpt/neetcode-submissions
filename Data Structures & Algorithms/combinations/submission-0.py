class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, current):
            if i > n:
                return

            current.append(i)
            if len(current) == k:
                copy = current.copy()
                res.append(copy)
            else:
                dfs(i + 1, current)
            current.pop()
            dfs(i + 1, current)

        start = []
        dfs(1, start)
        return res
            
