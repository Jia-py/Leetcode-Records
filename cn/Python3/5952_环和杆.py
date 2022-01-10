# @algorithm @lc id=2226 lang=python3 weekname=weekly-contest-271
# @title rings-and-rods


from cn.Python3.mod.preImport import *
# @test("B0B6G0R6R0R6G9")=1
# @test("B0R0G0R9R0B0G0")=1
# @test("G4")=0
class Solution:
    def countPoints(self, rings: str) -> int:
        dic = {}
        for i in range(len(rings)//2):
            if rings[2*i+1] not in dic:
                dic[rings[2*i+1]] = set()
            dic[rings[2*i+1]].add(rings[2*i])
        ans = []
        for i in dic:
            if len(dic[i]) == 3:
                ans.append(i)
        return len(ans)