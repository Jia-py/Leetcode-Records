# @algorithm @lc id=2234 lang=python3 weekname=weekly-contest-272
# @title minimum-operations-to-make-the-array-k-increasing


from cn.Python3.mod.preImport import *
# @test([5,4,3,2,1],1)=4
# @test([4,1,5,2,6,2],2)=0
# @test([4,1,5,2,6,2],3)=2
# @test([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3], 1)=12
# @test([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3], 1)=12
# @test([2,2,2,2,2,1,1,4,4,3,3,3,3,3], 1)=4
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        import bisect
        ans = 0
        def lengthOfLIS(nums: List[int]) -> int:
            # 这里lis[i]为长度为i+1的子序列末尾元素的最小值
            # 通过证明我们可以得知lis序列是严格递增的
            lis = [nums[0]]
            # 循环每个nums元素
            for num in nums[1:]:
                # 如果该元素大于lis中最后一个元素，说明最长子序列可以延长
                if num >= lis[-1]:
                    lis.append(num)
                # 否则说明不可以延长
                # 找到lis中第一个大于num的元素，替换
                # 这样我们优化了该长度下序列末尾的最小值
                else:
                    lis[bisect.bisect_right(lis, num)] = num
            # 最长非递减子序列的长度即为lis的长度
            return len(nums) - len(lis)


        for i in range(k):
            tmp_lis = arr[i::k]
            ans += lengthOfLIS(tmp_lis)
        return ans

