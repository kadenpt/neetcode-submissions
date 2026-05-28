class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = defaultdict(list)
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                res[j].append(matrix[i][j])
        
        return list(res.values())