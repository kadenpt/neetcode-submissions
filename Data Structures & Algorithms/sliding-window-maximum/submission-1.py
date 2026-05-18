class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # begin l at beginning of window
        for l in range(len(nums) - k + 1):
            current = []
            for r in range(l, l + k):
                current.append(nums[r])
            
            res.append(max(current))

        return res
            