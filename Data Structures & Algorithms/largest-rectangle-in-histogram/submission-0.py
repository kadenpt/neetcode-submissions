class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            # While the current height is smaller than the stack’s top height,
            # pop and calculate area for that previous height.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                maxArea = max(maxArea, height * width)
                start = index  # rectangle can start earlier than i
            stack.append((start, h))

        # Process remaining bars in stack
        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, h * width)

        return maxArea
