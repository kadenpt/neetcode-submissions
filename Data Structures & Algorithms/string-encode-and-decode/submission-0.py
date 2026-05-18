class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        # 4#neet4#code5#loves3#you
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # marks place in string
            j = i
            # keep track of how many letters to use
            while s[j] != '#':
                j += 1

            # calculate length of string
            length = int(s[i:j])

            # move i to index of first letter
            i = j + 1
            # set j as index of last letter
            j = i + length

            # append to res string
            res.append(s[i:j])
            i = j

        return res

