class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        most_common, most_freq = counts.most_common(1)[0]
        return most_common