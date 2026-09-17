class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res=[]
        for i in range(len(matrix)):
            r=[]
            for j in range(len(matrix)):
                r.insert(0,matrix[j][i])
            res.append(r)
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j]=res[i][j]
        