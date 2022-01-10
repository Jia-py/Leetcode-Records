# @algorithm @lc id=2232 lang=python3 weekname=weekly-contest-272
# @title adding-spaces-to-a-string


from cn.Python3.mod.preImport import *
# @test("LeetcodeHelpsMeLearn",[8,13,15])="Leetcode Helps Me Learn"
# @test("icodeinpython",[1,5,7,9])="i code in py thon"
# @test("spacing",[0,1,2,3,4,5,6])=" s p a c i n g"
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # s = list(s)
        # tmp = 0
        # for index in spaces:
        #     s.insert(index+tmp," ")
        #     tmp += 1
        # return "".join(s)
        s = list(s)
        for index in spaces:
            s[index] = " "+s[index]
        return "".join(s)
