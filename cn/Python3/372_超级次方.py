# @algorithm @lc id=372 lang=python3 
# @title super-pow


from cn.Python3.mod.preImport import *
# @test(2,[3])=8
# @test(2,[1,0])=1024
# @test(1,[4,3,3,8,5,2])=1
# @test(2147483647,[2,0,0])=1198
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a,int("".join(map(str,b))),1337)
