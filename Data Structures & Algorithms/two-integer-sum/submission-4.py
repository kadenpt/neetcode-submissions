class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v = {}
        for i in range(len(nums)):
            v[nums[i]] = i
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in v and v[tar] != i:
                return [i, v[tar]]
        return []