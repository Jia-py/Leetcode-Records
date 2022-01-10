# @algorithm @lc id=2254 lang=python3 weekname=weekly-contest-275
# @title check-if-every-row-and-column-contains-all-numbers


from cn.Python3.mod.preImport import *
# @test([[1,2,3],[3,1,2],[2,3,1]])=true
# @test([[1,1,1],[1,2,3],[1,2,3]])=false
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        lis = list(range(1,n+1))
        ans = True
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(matrix[i][j])
            if sorted(tmp) != lis:
                ans = False
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(matrix[j][i])
            if sorted(tmp) != lis:
                ans = False
        return ans

