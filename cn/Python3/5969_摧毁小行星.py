# @algorithm @lc id=2245 lang=python3 weekname=weekly-contest-274
# @title destroying-asteroids


from cn.Python3.mod.preImport import *
# @test(10,[3,9,19,5,21])=true
# @test(5,[4,9,23,4])=false
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        flag = True
        for i in range(len(asteroids)):
            if asteroids[i] <= mass:
                mass = asteroids[i] + mass
            else:
                return False
        return True