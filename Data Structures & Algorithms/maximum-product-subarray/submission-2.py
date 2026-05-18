class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = nums[0]

        for l in range(len(nums)):
            current = nums[l]
            if current > res:
                res = current
            for r in range(l + 1, len(nums)):
                current *= nums[r]
                if current > res:
                    res = current
        
        return res