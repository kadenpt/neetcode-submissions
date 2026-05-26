class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(total, i):
            if i >= n:
                return total
            
            if memo[i] != -1:
                return total + memo[i]

            memo[i] = max(
                dfs(total, i + 1),
                dfs(total + nums[i], i + 2))
            return total + memo[i]
        
        return dfs(0, 0)