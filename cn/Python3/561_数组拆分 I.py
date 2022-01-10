# @algorithm @lc id=561 lang=python3 
# @title array-partition-i


from cn.Python3.mod.preImport import *
# @test([1,4,3,2])=4
# @test([6,2,6,5,1,2])=9
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[::2])