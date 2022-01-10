# @algorithm @lc id=27 lang=python3 
# @title remove-element


from cn.Python3.mod.preImport import *
# @test([3,2,2,3],3)=2
# @test([0,1,2,2,3,0,4,2],2)=5
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow