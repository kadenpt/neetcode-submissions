class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            # count number of times s[r] has appeared
            count[s[r]] = 1 + count.get(s[r], 0)
            #update maxf with most freq character appearance
            maxf = max(maxf, count[s[r]])

            # check if window is valid
            # if window is valid, k replacements can turn substring
            # to one letter
            while (r - l + 1) - maxf > k:
                # decrease from left
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
        
        