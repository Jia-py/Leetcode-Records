# @algorithm @lc id=881 lang=python3 
# @title loud-and-rich


from cn.Python3.mod.preImport import *
# @test([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]],[3,2,5,4,6,1,7,0])=[5,5,2,5,4,5,6,7]
# @test([],[0])=[0]
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        