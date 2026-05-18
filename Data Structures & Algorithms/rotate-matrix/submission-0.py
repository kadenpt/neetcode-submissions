class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # reverse matrix vertically
        l, r = 0, len(matrix) - 1
        while l < r:
            temp = matrix[l]
            matrix[l] = matrix[r]
            matrix[r] = temp
            l += 1
            r -= 1
        
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]