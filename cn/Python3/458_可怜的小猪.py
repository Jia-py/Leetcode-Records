# @algorithm @lc id=458 lang=python3 
# @title poor-pigs


from cn.Python3.mod.preImport import *
# @test(1000,15,60)=5
# @test(4,15,15)=2
# @test(4,15,30)=2
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest // minutesToDie
        ans = 0
        product = 1
        while product < buckets:
            product *= (times + 1)
            ans += 1
        return ans