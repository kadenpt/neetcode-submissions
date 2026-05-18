class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        
        for l in range(len(nums)):
            current = nums[l]

            r = l + 1
            while r < len(nums):
                current += nums[r]
                res = max(current, res)
                r += 1
            
            res = max(current, res)

        return res