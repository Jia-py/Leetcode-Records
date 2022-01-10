# @algorithm @lc id=2204 lang=python3 weekname=biweekly-contest-67
# @title find-subsequence-of-length-k-with-the-largest-sum


from cn.Python3.mod.preImport import *
# @test([2,1,3,3],2)=[3,3]
# @test([-1,-2,3,4],3)=[-1,3,4]
# @test([3,4,3,3],2)=[3,4]
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lis = sorted(range(len(nums)),key = lambda x:nums[x], reverse=True)
        k_lis = sorted(lis[:k])
        return [nums[i] for i in k_lis]