class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        for l in range(len(s)):
            current = s[l]
            r = l + 1
            while r < len(s):
                if s[r] not in current:
                    current += s[r]
                    res = max(len(current), res)
                else:
                    current = s[r]
                r += 1
        return res