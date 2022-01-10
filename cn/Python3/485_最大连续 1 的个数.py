# @algorithm @lc id=485 lang=python3 
# @title max-consecutive-ones


from cn.Python3.mod.preImport import *
# @test([1,1,0,1,1,1])=3
# @test([1,0,1,1,0,1])=2
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        ans = 0
        for right in range(len(nums)):
            if nums[right] != 1:
                ans = max(ans,right-left-1)
                left = right
            if right == len(nums)-1 and nums[-1] == 1:
                ans = max(ans,right-left)
        return ans
        '''
        他人的解法，可以不用判断最后的边界条件
        index = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                index = i
            else:
                res = max(res, i - index)
        return res
        '''
        
