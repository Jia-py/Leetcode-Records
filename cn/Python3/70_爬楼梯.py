# @algorithm @lc id=70 lang=python3 
# @title climbing-stairs


from cn.Python3.mod.preImport import *
# @test(2)=2
# @test(3)=3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        lis = [0]*n
        lis[0],lis[1] = 1,2
        for i in range(2,n):
            lis[i] = lis[i-1] + lis[i-2]
        return lis[-1]