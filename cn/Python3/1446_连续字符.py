# @algorithm @lc id=1542 lang=python3 
# @title consecutive-characters


from cn.Python3.mod.preImport import *
# @test("leetcode")=2
# @test("abbcccddddeeeeedcba")=5
# @test("triplepillooooow")=5
# @test("hooraaaaaaaaaaay")=11
# @test("tourist")=1
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        former = ''
        leng = 1
        for i in s:
            if i != former:
                leng = 1
                former = i
            else:
                leng += 1
            if leng > ans:
                ans = leng
        return ans