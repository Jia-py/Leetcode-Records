# @algorithm @lc id=2255 lang=python3 weekname=weekly-contest-275
# @title minimum-swaps-to-group-all-1s-together-ii


from cn.Python3.mod.preImport import *
# @test([0,1,0,1,1,0,0])=1
# @test([0,1,1,1,0,0,1,1,0])=2
# @test([1,1,0,0,1])=0
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ans = 1e9
        count_1 = nums.count(1)
        # 第一步
        tmp_count_1 = nums[0:count_1].count(1)
        ans = min(ans,count_1 - tmp_count_1)
        for i in range(1,len(nums)-count_1+1):
            if nums[i-1] == 1:
                tmp_count_1 -= 1
            if nums[i+count_1-1] == 1:
                tmp_count_1 += 1
            ans = min(ans,count_1 - tmp_count_1)
        # 第一步
        count_0 = nums.count(0)
        tmp_count_0 = nums[0:count_0].count(0)
        ans = min(ans,count_0 - tmp_count_0)
        for i in range(1,len(nums)-count_0+1):
            if nums[i-1] == 0:
                tmp_count_0 -= 1
            if nums[i+count_0-1] == 0:
                tmp_count_0 += 1
            ans = min(ans,count_0 - tmp_count_0)
        return ans