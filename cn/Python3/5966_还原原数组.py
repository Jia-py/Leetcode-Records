# @algorithm @lc id=2241 lang=python3 weekname=weekly-contest-273
# @title recover-the-original-array


from cn.Python3.mod.preImport import *
# @test([2,10,6,4,8,12])=[3,7,11]
# @test([1,1,3,3])=[2,2]
# @test([5,435])=[220]
# @test([11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9])=[2,3,7,8,8,9,9,10]
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        lowerest = nums[0]
        for j in range(1,len(nums)):
            diff = nums[j] - lowerest
            if diff <= 0 or diff % 2 == 1:
                continue
            n = len(nums)
            slow = 0
            fast = 0
            lower_arr = []
            higher_arr = []
            visited = [False] * n
            while fast < len(nums) and slow < len(nums):
                while visited[fast] == True or nums[fast] != nums[slow] + diff:
                    fast += 1
                    if fast == len(nums):
                        break
                if fast == len(nums):
                    break
                lower_arr.append(nums[slow])
                higher_arr.append(nums[fast])
                visited[slow],visited[fast] = True,True
                while visited[slow] == True:
                    slow += 1
                    if slow == len(nums):
                        break
            if len(lower_arr) == len(higher_arr) == n/2:
                return [int(x + diff/2) for x in lower_arr]
                
