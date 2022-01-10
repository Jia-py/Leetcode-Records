# @algorithm @lc id=198 lang=python3 
# @title house-robber


from cn.Python3.mod.preImport import *
# @test([1,2,3,1])=4
# @test([2,7,9,3,1])=12
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lis = [None]*len(nums)
        lis[0] = nums[0]
        lis[1] = max(nums[0:2])
        for i in range(2,len(nums)):
            lis[i] = max(lis[i-2] + nums[i],lis[i-1])
        return lis[-1]