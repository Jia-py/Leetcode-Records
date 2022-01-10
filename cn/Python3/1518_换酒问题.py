# @algorithm @lc id=1642 lang=python3 
# @title water-bottles


from cn.Python3.mod.preImport import *
# @test(9,3)=13
# @test(15,4)=19
# @test(5,5)=6
# @test(2,3)=2
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            ans += numBottles//numExchange
            numBottles = numBottles//numExchange + numBottles % numExchange
        return ans