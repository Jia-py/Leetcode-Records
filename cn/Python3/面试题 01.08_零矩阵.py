# @algorithm @lc id=100186 lang=python3 
# @title zero-matrix-lcci


from cn.Python3.mod.preImport import *
# @test([[1,1,1],[1,0,1],[1,1,1]])=[[1,0,1],[0,0,0],[1,0,1]]
# @test([[0,1,2,0],[3,4,5,2],[1,3,1,5]])=[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# @test([[0,1,2,0],[3,4,5,2],[1,3,1,5]])=[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zero_list = [(x,y) for x in range(n) for y in range(m) if matrix[x][y] == 0]
        print(zero_list)
        for x,y in zero_list:
            for i in range(n):
                matrix[i][y] = 0
            for i in range(m):
                matrix[x][i] = 0
        return matrix