# @algorithm @lc id=1039 lang=python3 
# @title find-the-town-judge


from cn.Python3.mod.preImport import *
# @test(2,[[1,2]])=2
# @test(3,[[1,3],[2,3]])=3
# @test(3,[[1,3],[2,3],[3,1]])=-1
# @test(1, [])=1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        # 存放有相信他人的人
        lis = set()
        # 以被相信人为key，统计相信他的人有多少
        dic = {}
        for x,y in trust:
            if y not in dic:
                dic[y] = 0
            dic[y] += 1
            lis.add(x)
        for key in dic:
            # 如果有n-1的人相信他，且他不相信任何人，则他是法官
            if dic[key] == n-1 and key not in lis:
                return key
        return -1