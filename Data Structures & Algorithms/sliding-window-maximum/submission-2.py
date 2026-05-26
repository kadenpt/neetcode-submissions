class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            right = min(i + k, len(nums))
            res.append(max(nums[i:right]))
        return res