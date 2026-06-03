class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        benchmark = len(nums) // 3
        count = Counter(nums)
        for k, v in count.items():
            if v > benchmark:
                res.append(k)

        return res