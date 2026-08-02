class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        targSum = sum(nums) // k

        nums.sort(reverse=True)

        def backtrack(groups, i):
            if i == len(nums):
                return True
            
            for j in range(k):
                groups[j] += nums[i]
                if groups[j] <= targSum:
                    if backtrack(groups, i + 1):
                        return True
                groups[j] -= nums[i]
                if groups[j] == 0:
                    break
            return False
        
        groups = [0] * k
        return backtrack(groups, 0)