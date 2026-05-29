class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            if (i != len(s) - 1) and (s[i] == 'I' and(s[i + 1] == 'V' or s[i + 1] == 'X')) or (s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or (s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                total += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i += 1

        return total
