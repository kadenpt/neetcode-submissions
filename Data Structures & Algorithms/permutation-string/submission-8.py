class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLength = len(s1)
        count = {}
        # populate dict with s1 freqs
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        print(count)

        print(s2)
        for r in range(len(s2) - windowLength + 1):
            count2 = {}
            maxPossible = r + windowLength
            for j in range(r, maxPossible):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
            print( count2)
            if count2 == count:
                return True

        return False





        