# @algorithm @lc id=2257 lang=python3 weekname=weekly-contest-275
# @title earliest-possible-day-of-full-bloom


from cn.Python3.mod.preImport import *
# @test([1,4,3],[2,3,1])=9
# @test([1,2,3,2],[2,1,2,1])=9
# @test([1],[1])=2
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        order = sorted(range(len(growTime)),key = lambda x:growTime[x],reverse = True)
        max_time = 0
        time = 0
        for i in order:
            plant_time = plantTime[i]
            grow_time = growTime[i]
            time += plant_time
            max_time = max(max_time, time + grow_time)
        return max_time