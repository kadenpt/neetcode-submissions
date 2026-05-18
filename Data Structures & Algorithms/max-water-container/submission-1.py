class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for l in range(len(heights)):
            for r in range(l, len(heights)):
                width = r - l
                height = min(heights[l], heights[r])
                volume = width * height
                res = max(res, volume)

        return res