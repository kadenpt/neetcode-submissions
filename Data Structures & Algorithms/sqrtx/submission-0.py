class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            res = mid * mid
            if res > x:
                r = mid - 1
            elif res < x:
                l = mid + 1
            else:
                return mid
        
        return l - 1