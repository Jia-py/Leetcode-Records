# @algorithm @lc id=686 lang=python3 
# @title repeated-string-match


from cn.Python3.mod.preImport import *
# @test("abcd","cdabcdab")=3
# @test("a","aa")=2
# @test("a","a")=1
# @test("abc","wxyz")=-1
# @test("aaaaaaaaaaaaaaaaaaaaaab", "ba")=2
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = len(b) // len(a)
        for i in range(times,times+3):
            tmp = i*a
            if b in tmp:
                return i
        return -1
        