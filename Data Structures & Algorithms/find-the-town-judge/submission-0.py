class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustArray = [0] * (n + 1)
        for i in range(len(trust)):
            trustArray[trust[i][0]] -= 1
            trustArray[trust[i][1]] += 1
        
        for i in range(len(trustArray)):
            if trustArray[i] == n - 1:
                return i
        
        return -1