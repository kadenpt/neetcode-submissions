class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        initLength = len(nums)
        for i in range(initLength):
            nums.append(nums[i])

        return nums