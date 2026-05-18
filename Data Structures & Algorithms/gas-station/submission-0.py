class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        def dfs(start, current, fuel):
            fuel -= cost[current]

            if fuel < 0:
                return False

            # Successfully moved to next station
            current += 1

            if current >= len(gas):
                current = 0
            
            if current == start:
                return True

            # fill tank
            fuel += gas[current]

            return dfs(start, current, fuel)

            
        
        res = -1
        for i in range(len(gas)):
            if gas[i] < cost[i]:
                pass
            elif dfs(i, i, gas[i]):
                res = i
                break
        
        return res