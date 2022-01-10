# @algorithm @lc id=2212 lang=python3 weekname=weekly-contest-269
# @title removing-minimum-and-maximum-from-array


from cn.Python3.mod.preImport import *
# @test([2,10,7,5,4,1,8,6])=5
# @test([0,-4,19,1,8,-2,-3,5])=3
# @test([101])=1
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        if min_index > max_index:
            right_index = min_index
            left_index = max_index
        else:
            right_index = max_index
            left_index = min_index
        #先删最小值
        dis1 = left_index + 1
        dis2 = right_index - left_index
        dis3 = len(nums) - right_index
        sum1 = dis1+dis2
        sum2 = dis1+dis3
        sum3 = dis2+dis3
        return min([sum1,sum2,sum3])
