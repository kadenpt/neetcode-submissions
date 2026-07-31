class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        maxLen = sum(matchsticks) / 4
        if sum(matchsticks) % 4 != 0 or max(matchsticks) > maxLen:
            return False

        def backtrack(sides, i):
            if sides[0] == sides[1] == sides[2] == sides[3] and i >= len(matchsticks):
                return True
            if i >= len(matchsticks):
                return False
            
            for j in range(len(sides)):
                if sides[j] + matchsticks[i] <= maxLen:
                    sides[j] += matchsticks[i]
                    if backtrack(sides, i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        
        return backtrack([0, 0, 0, 0], 0)