# @algorithm @lc id=1047 lang=python3 
# @title maximize-sum-of-array-after-k-negations


from cn.Python3.mod.preImport import *
# @test([4,2,3],1)=5
# @test([3,-1,0,2],3)=6
# @test([2,-3,-1,5,-4],2)=13
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        nega_num = 0
        for i in nums:
            if i < 0 :
                nega_num += 1
        if k > nega_num:
            if (k-nega_num)%2 == 0:
                return sum(list(map(abs,nums)))
            else:
                nums = sorted(list(map(abs,nums)))
                nums[0] = -nums[0]
                return sum(nums)
        elif k <= nega_num:
            for i in range(k):
                nums[i] = -nums[i]
            return sum(nums) 