# @algorithm @lc id=2200 lang=python3 weekname=biweekly-contest-69
# @title stamping-the-grid


from cn.Python3.mod.preImport import *
# @test([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]],4,3)=true
# @test([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],2,2)=false
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[[0,0]] * n for _ in range(m) ]
        # dp[0][0] = [1,1]
        # for i in range()
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             dp[i][j][0] = min(dp[i-1][j][0],dp[i][j-1][0])
        #             dp[i][j][1] = min(dp[i-1][j][1],dp[i][j-1][1])
        #         elif grid[i-1][j] == 1 and grid[i][j-1] != 1:
        #             dp[i][j][0] = 1
        #             dp[i][j][1] = min(dp[i-1][j][1],dp[i][j-1][1]) + 1
        #         elif grid[i][j-1] == 1 and grid[i-1][j] != 1:
        #             dp[i][j][1] = 1
        #             dp[i][j][0] = min(dp[i-1][j][0],dp[i][j-1][0]) + 1
        #         elif grid[i-1][j] == 1 and grid[i][j-1] == 1:
        #             dp[i][j] = [1,1]
        #         else:
        #             dp[i][j][0] = max(dp[i-1][j][0],dp[i][j-1][0])
        #             dp[i][j][1] = max(dp[i-1][j][1],dp[i][j-1][1])
        # if dp[-1][-1][0] >= stampHeight and dp[-1][-1][1] >= stampWidth:
        #     return True
        # else:
        #     return False

