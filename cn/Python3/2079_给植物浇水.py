# @algorithm @lc id=1310 lang=python3 weekname=weekly-contest-268
# @title watering-plants


from cn.Python3.mod.preImport import *
# @test([2,2,3,3],5)=14
# @test([1,1,1,4,2,3],4)=30
# @test([7,7,7,7,7,7,7],8)=49
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int: