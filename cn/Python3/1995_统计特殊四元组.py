# @algorithm @lc id=2122 lang=python3 
# @title count-special-quadruplets


from cn.Python3.mod.preImport import *
# @test([1,2,3,6])=1
# @test([3,3,6,4,5])=0
# @test([1,1,1,3,5])=4
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for x in range(j+1,len(nums)):
                    for z in range(x+1,len(nums)):
                        if nums[i] + nums[j] + nums[x] == nums[z]:
                            ans += 1
        return ans