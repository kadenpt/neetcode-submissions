class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, total):
            if i >= len(nums):
                return 0

            if i == len(nums) - 1:
                if total + nums[i] == target and total - nums[i] == target:
                    return 2
                if total + nums[i] == target or total - nums[i] == target:
                    return 1
            
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)