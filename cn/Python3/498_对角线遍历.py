# @algorithm @lc id=498 lang=python3 
# @title diagonal-traverse


from cn.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=[1,2,4,7,5,3,6,8,9]
# @test([[1,2],[3,4]])=[1,2,3,4]
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ans = []
        for i in range(m+n-1):
            x = 0 if i < n else i -n + 1
            y = i if i<n else n - 1
            tmp = []
            while 0<=x<m and 0<=y<n:
                tmp.append(mat[x][y])
                x += 1
                y -= 1
            if i%2 == 0:
                tmp.reverse()
                ans.extend(tmp)
            else:
                ans += tmp
        return ans


            

