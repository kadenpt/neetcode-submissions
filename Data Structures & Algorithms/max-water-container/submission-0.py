class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        # find the max width and max height
        l, r = 0, len(heights) - 1
        while l < r:
            total = (r - l) * min(heights[l], heights[r])
            if total > maxarea:
                maxarea = total
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxarea

    