class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        table = list(set(nums))
        for i in range(len(table)):
            startNum = table[i]
            length = 1
            distance = 1
            while True:
                if startNum + distance in table:
                    length += 1
                    distance += 1
                else:
                    break

            if length > res:
                res = length

        return res
