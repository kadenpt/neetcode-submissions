class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = 1
        for i in range(abs(n)):
            base *= x
        
        if n > 0:
            return base
        else:
            return (1 / base)
