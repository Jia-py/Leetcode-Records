# @algorithm @lc id=400 lang=python3 
# @title nth-digit


from cn.Python3.mod.preImport import *
# @test(3)=3
# @test(11)=0
class Solution:
    def findNthDigit(self, n: int) -> int:
        step = 0
        number = 1
        while step < n:
            tmp = str(number)
            for character in tmp:
                step += 1
                if step == n:
                    return int(character)
            number += 1
        