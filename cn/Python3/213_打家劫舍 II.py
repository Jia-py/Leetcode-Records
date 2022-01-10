# @algorithm @lc id=213 lang=python3 
# @title house-robber-ii


from cn.Python3.mod.preImport import *
# @test([2,3,2])=3
# @test([1,2,3,1])=4
# @test([1,2,3])=3
class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums):
            if len(nums) == 1:
                return nums[0]
            lis = [None]*len(nums)
            lis[0] = nums[0]
            lis[1] = max(nums[0:2])
            for i in range(2,len(nums)):
                lis[i] = max(lis[i-2] + nums[i],lis[i-1])
            return lis[-1]
        if len(nums) == 1: return nums[0]
        lis1 = nums[:-1]
        lis2 = nums[1:]
        return max(solve(lis1),solve(lis2))