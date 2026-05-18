class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)
        res = upper

        while lower <= upper:
            k = ((upper + lower) // 2)
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                upper = k - 1
            else: 
                lower = k + 1
        return res
