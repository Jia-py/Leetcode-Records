# @algorithm @lc id=2233 lang=python3 weekname=weekly-contest-272
# @title number-of-smooth-descent-periods-of-a-stock


from cn.Python3.mod.preImport import *
# @test([3,2,1,4])=7
# @test([8,6,7,7])=4
# @test([1])=1
# @test([3,2,1,4])=7
# @test([3,2,1,4])=7
# @test([3,2,1,4])=7
# @test([3,2,1,4])=7
# @test([12,11,10,9,8,7,6,5,4,3,4,3,10,9,8,7])=68
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 1
        ans = 0
        tmp = 1
        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i] == prices[i-1] - 1:
                tmp += 1
            else:
                ans += (tmp + 1)*tmp /2
                tmp = 1
        ans += (tmp + 1)*tmp /2
        return int(ans)

            

