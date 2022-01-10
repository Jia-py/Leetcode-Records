# @algorithm @lc id=949 lang=python3 
# @title cat-and-mouse


from cn.Python3.mod.preImport import *
# @test([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]])=0
# @test([[1,3],[0],[3],[0,2]])=1
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        