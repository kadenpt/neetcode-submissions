class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
            
        left = 0
        running_sum = 0
        min_length = float('inf')
        
        # 'right' expands the window
        for right in range(len(nums)):
            running_sum += nums[right]
            
            # Shrink the window from the left as long as the condition is met
            while running_sum >= target:
                # Calculate current window size: (right - left + 1)
                min_length = min(min_length, right - left + 1)
                
                # Shrink window from left and update the running sum
                running_sum -= nums[left]
                left += 1
                
        return min_length if min_length != float('inf') else 0