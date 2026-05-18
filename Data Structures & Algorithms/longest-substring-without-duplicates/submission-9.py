class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        length = 1
        # current = substring
        current = s[l]

        while r < len(s):
            # current substring finds duplicate
            # evaluate substrings starting at next char
            if s[r] in current:
                current = s[l + 1]
                l += 1
                r = l + 1
            ## continue adding to substring
            else:
                current += s[r]
                r += 1
            length = max(length, len(current))

        return length
        