class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        start = len(digits) - 1
        while start >= 0 or carry > 0:
            if start >= 0:
                add = digits[start] + carry
                if add == 10:
                    res.append(0)
                    carry = 1
                else:
                    res.append(add)
                    carry = 0
                start -= 1
            else:
                res.append(carry)
                carry -= 1
            

        return res[::-1]
