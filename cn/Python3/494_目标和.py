# @algorithm @lc id=494 lang=python3 
# @title target-sum


from cn.Python3.mod.preImport import *
# @test([1,1,1,1,1],3)=5
# @test([1],1)=1
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        def dfs(cur_index, sum):
            nonlocal ans
            if cur_index == len(nums) - 1:
                if sum == target: ans += 1
                return
            
            dfs(cur_index+1, sum+nums[cur_index+1])
            dfs(cur_index+1, sum-nums[cur_index+1])
        dfs(-1,0)
        return ans