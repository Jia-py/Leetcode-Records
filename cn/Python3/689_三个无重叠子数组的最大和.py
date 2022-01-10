# @algorithm @lc id=689 lang=python3 
# @title maximum-sum-of-3-non-overlapping-subarrays


from cn.Python3.mod.preImport import *
# @test([1,2,1,2,6,7,5,1],2)=[0,3,5]
# @test([1,2,1,2,1,2,1,2,1],2)=[0,2,4]
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
