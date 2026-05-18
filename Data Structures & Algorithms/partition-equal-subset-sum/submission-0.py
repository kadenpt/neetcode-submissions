class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        def dfs(s1, s2, i):
            if (i == len(nums) and sum(s1) == sum(s2)):
                return True
            
            if i == len(nums):
                return False
            
            return (dfs(s1 + [nums[i]], s2, i + 1)
                or dfs(s1, s2 + [nums[i]], i + 1))

        return dfs([], [], 0)
