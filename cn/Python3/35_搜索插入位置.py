# @algorithm @lc id=35 lang=python3 
# @title search-insert-position


from cn.Python3.mod.preImport import *
# @test([1,3,5,6],5)=2
# @test([1,3,5,6],2)=1
# @test([1,3,5,6],7)=4
# @test([1,3,5,6],0)=0
# @test([1],0)=0
# @test([1], 1)=0
# @test([1,3], 3)=1
# @test([1,1], 1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target: return 0
        if nums[-1] < target: return len(nums)
        

        left = 0
        right = len(nums) - 1
        while left < right:
            # 取中间数靠左的索引
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left