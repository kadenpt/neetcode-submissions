class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [-1, -1, -1]

        for i in range(len(triplets)):
            if target[0] < triplets[i][0]:
                pass
            elif target[1] < triplets[i][1]:
                pass
            elif target[2] < triplets[i][2]:
                pass
            else:
                res = [max(res[0], triplets[i][0]),
                        max(res[1], triplets[i][1]),
                        max(res[2], triplets[i][2])]

            if res == target:
                return True
            
        return False