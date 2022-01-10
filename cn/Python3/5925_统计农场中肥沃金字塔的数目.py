# @algorithm @lc id=2193 lang=python3 weekname=biweekly-contest-66
# @title count-fertile-pyramids-in-a-land


from cn.Python3.mod.preImport import *
# @test([[0,1,1,0],[1,1,1,1]])=2
# @test([[1,1,1],[1,1,1]])=2
# @test([[1,0,1],[0,0,0],[1,0,1]])=0
# @test([[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]])=13
class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int: