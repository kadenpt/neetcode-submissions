class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        
        for q in range(len(queries)):
            res = 10000
            for i in range(len(intervals)):
                if intervals[i][0] <= queries[q] and queries[q] <= intervals[i][1]:
                    length = intervals[i][1] - intervals[i][0] + 1
                    
                    res = min(length, res)
            if res == 10000:
                ans.append(-1)
            else: ans.append(res)

        return ans