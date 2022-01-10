# @algorithm @lc id=2243 lang=python3 weekname=weekly-contest-274
# @title check-if-all-as-appears-before-all-bs


from cn.Python3.mod.preImport import *
# @test("aaabbb")=true
# @test("abab")=false
# @test("bbb")=true
class Solution:
    def checkString(self, s: str) -> bool:
        index_a = None
        index_b = None
        for i in range(len(s)):
            if s[i] == 'a':
                index_a = i
        if 'b' in s:
            index_b = s.index('b')
        if index_a == None or index_b == None:
            return True
        if index_a > index_b:
            return False
        return True