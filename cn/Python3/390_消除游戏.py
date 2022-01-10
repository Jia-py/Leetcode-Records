# @algorithm @lc id=390 lang=python3 
# @title elimination-game


from cn.Python3.mod.preImport import *
# @test(9)=6
# @test(1)=1
class Solution:
    def lastRemaining(self, n: int) -> int:
        lis = list(range(1,n+1))
        flag = -1
        while len(lis)>1:
            flag = -flag
            if flag == 1:
                lis = lis[1::2]
            elif flag == -1:
                lis = lis[-2::-2][::-1]
        return lis[0]