# @algorithm @lc id=825 lang=python3 
# @title max-increase-to-keep-city-skyline


from cn.Python3.mod.preImport import *
# @test([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])=35
# @test([[0,0,0],[0,0,0],[0,0,0]])=0
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = [max(i) for i in grid]
        column = [max([item[i] for item in grid]) for i in range(len(grid[0]))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min(row[i],column[j]) - grid[i][j])
        return ans