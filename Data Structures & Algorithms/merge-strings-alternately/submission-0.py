class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        c1, c2 = 0, 0
        w1, w2 = len(word1), len(word2)
        for i in range(min(w1, w2)):
            res += word1[i]
            res += word2[i]
            c1 += 1
            c2 += 1
        
        while c1 < w1:
            res += word1[c1]
            c1 += 1
        
        while c2 < w2:
            res += word2[c2]
            c2 += 1
        
        return res