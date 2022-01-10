# @algorithm @lc id=2211 lang=python3 weekname=weekly-contest-269
# @title k-radius-subarray-averages


from cn.Python3.mod.preImport import *
# @test([7,4,3,9,1,8,5,2,6],3)=[-1,-1,-1,5,4,4,-1,-1,-1]
# @test([100000],0)=[100000]
# @test([8],100000)=[-1]
# @test([18334,25764,19780,92480,69842,73255,89893], 0)=[18334,25764,19780,92480,69842,73255,89893]
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = []
        length = (1+2*k)
        sum_ = 0
        for index in range(len(nums)):
            if 0<=index-k and index+k<len(nums):
                if index-k == 0:
                    sum_ = sum(nums[0:length])
                elif index+k == len(nums) - 1:
                    sum_ = sum(nums[index-k:])
                else:
                    sum_ += nums[index+k]
                    sum_ -= nums[index-k-1]
                ans.append(sum_//length)
            else:
                ans.append(-1)
        return ans
