class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        # digitToChar["2"][0] = a

        if len(digits) == 0:
            return []
        
        def backtrack(i, cur):
            if len(cur) >= len(digits):
                res.append(cur)
                return

            j = 0
            while j < len(digitToChar[digits[i]]):
                cur += digitToChar[digits[i]][j]
                backtrack(i + 1, cur)
                cur = cur[:-1]
                j += 1

            # cur += digitToChar[digits[i]][0]
            # backtrack(i + 1, cur)
            # cur = cur[:-1]
            # cur += digitToChar[digits[i]][1]
            # backtrack(i + 1, cur)
            # cur = cur[:-1]
            # cur += digitToChar[digits[i]][2]
            # backtrack(i + 1, cur)

        backtrack(0, "")
        return res