# @algorithm @lc id=2227 lang=python3 weekname=weekly-contest-271
# @title sum-of-subarray-ranges


from cn.Python3.mod.preImport import *
# @test([1,2,3])=4
# @test([1,3,3])=4
# @test([4,-2,-3,4,1])=59
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            max_ = 0
            min_ = 9999
            for j in range(i,len(nums)):
                if j > max_: max_ = j
                if j < min_: min_ = j
                ans += (max_ - min_)
        return ans