# @algorithm @lc id=2210 lang=python3 weekname=weekly-contest-269
# @title find-target-indices-after-sorting-array


from cn.Python3.mod.preImport import *
# @test([1,2,5,2,3],2)=[1,2]
# @test([1,2,5,2,3],3)=[3]
# @test([1,2,5,2,3],5)=[4]
# @test([1,2,5,2,3],4)=[]
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lis = sorted(nums)
        ans = []
        for index,i in enumerate(lis):
            if i == target:
                ans.append(index)
        return ans