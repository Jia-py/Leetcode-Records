# @algorithm @lc id=167 lang=python3 
# @title two-sum-ii-input-array-is-sorted


from cn.Python3.mod.preImport import *
# @test([2,7,11,15],9)=[1,2]
# @test([2,3,4],6)=[1,3]
# @test([-1,0],-1)=[1,2]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left+1,right+1]
        