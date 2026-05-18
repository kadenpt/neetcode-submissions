class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if 1 == ((n >> i) & 1):
                res |= (1 << (31 - i))

        return res