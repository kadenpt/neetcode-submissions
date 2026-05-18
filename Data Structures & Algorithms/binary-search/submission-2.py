class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # m = middle of array
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            # target is in top half
            if nums[m] < target:
                l= m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return -1

