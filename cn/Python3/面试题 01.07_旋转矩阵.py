# @algorithm @lc id=100185 lang=python3 
# @title rotate-matrix-lcci


from cn.Python3.mod.preImport import *
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 旋转解法，将图形切块旋转
        n = len(matrix)
        height = n // 2 
        width = (n+1) // 2
        for i in range(height):
            for j in range(width):
                matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = \
                    matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
        # 另外可以使用水平翻转接斜对角翻转完成旋转操作