matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
class Solution:
    def setZeroes(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        row_track=[0]*m
        col_track=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_track[i]=-1
                    col_track[j]=-1
                    
        for i in range(m):
            for j in range(n):
                if row_track[i]==-1 or col_track[j]==-1:
                    matrix[i][j]=0
        return matrix
s=Solution()
print(s.setZeroes(matrix))