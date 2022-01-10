# @algorithm @lc id=747 lang=python3 
# @title min-cost-climbing-stairs


from cn.Python3.mod.preImport import *
# @test([10,15,20])=15
# @test([1,100,1,1,1,100,1,1,100,1])=6
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lis = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            lis[i] = min(lis[i-1]+cost[i-1],lis[i-2]+cost[i-2])
        return lis[-1]