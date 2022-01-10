# @algorithm @lc id=740 lang=python3 
# @title delete-and-earn


from cn.Python3.mod.preImport import *
# @test([3,4,2])=6
# @test([2,2,3,3,3,4])=9
# @test([4,10,10,8,1,4,10,9,7,6])=53
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        import collections
        counter = collections.Counter(nums)
        lis = sorted(list(set(counter.keys())))
        if len(lis) == 1:
            return counter[lis[0]]*lis[0]
        dp = [None]*max(lis)
        dp[0] = counter[1]*1
        dp[1] = max(dp[0],counter[2]*2)
        for i in range(2,max(lis)):
            dp[i] = max(dp[i-2]+counter[i+1]*(i+1),dp[i-1])
        return dp[-1]
        

