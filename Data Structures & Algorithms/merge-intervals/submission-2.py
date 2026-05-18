class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = []
        def dfs(start, end, i):
            if i >= len(intervals):
                res.append([start, end])
                return

            if start == intervals[i][0] or end >= intervals[i][0]:
                dfs(start, max(end, intervals[i][1]), i + 1)
            else:
                res.append([start, end])
                dfs(intervals[i][0], intervals[i][1], i + 1)


        dfs(intervals[0][0], intervals[0][1], 1)
        return res