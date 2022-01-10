# @algorithm @lc id=209 lang=python3 
# @title minimum-size-subarray-sum


from cn.Python3.mod.preImport import *
# @test(7,[2,3,1,2,4,3])=2
# @test(4,[1,4,4])=1
# @test(11,[1,1,1,1,1,1,1,1])=0
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 对应官方题解的第三种方法，滑动窗口
        # 但写while的时候结构不够精妙
        if sum(nums) < target:
            return 0
        ans = int(1e9)
        left = -1
        tmp_sum = 0
        right = -1
        while right < len(nums)-1:
            while tmp_sum < target and right < len(nums)-1:
                right += 1
                tmp_sum += nums[right]
            ans = min(ans,right-left)
            while tmp_sum >= target:
                left += 1
                tmp_sum -= nums[left]
                if tmp_sum >= target:
                    ans = min(ans,right-left)
        return ans
            
