class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        
        for index, val in enumerate(nums):
            # if min val is positive, 0 true cases
            if val > 0: break

            # skip duplicates
            if index > 0 and val == nums[index - 1]:
                continue
            
            l, r = index+1, len(nums) - 1
            while l<r:
                threeSum = nums[index] + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    sol.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1


        return sol

            

