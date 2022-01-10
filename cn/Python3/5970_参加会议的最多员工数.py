# @algorithm @lc id=2246 lang=python3 weekname=weekly-contest-274
# @title maximum-employees-to-be-invited-to-a-meeting


from cn.Python3.mod.preImport import *
# @test([2,2,1,2])=3
# @test([1,2,0])=3
# @test([3,0,1,4,1])=4
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        dic = {}
        max_i,max = 0,0
        for i in range(len(favorite)):
            if favorite[i] not in dic:
                dic[favorite[i]] = [[],0]
            dic[favorite[i]][0].append(i)
            dic[favorite[i]][1] += 1
            if dic[favorite[i]][1] > max:
                max = dic[favorite[i]][1]
                max_i = i
        for key in dic:
            dic[key][0] = sorted(dic[key][0],key = lambda x:dic[x][1],reverse=False)
        ans = 0
        node = max_i
        if len(dic[node][0]) == 0:
            return 1
        elif len(dic[node][0]) == 1:
            while len(dic[node][0])>0:
                ans += 1
                node = dic[node][0][0]
        elif len(dic[node][0]) == 2:
            ans += 1
            node = dic[max_i][0][0]
            while len(dic[node][0])>0:
                ans += 1
                node = dic[node][0][0]
            node = dic[max_i][0][1]
            while len(dic[node][0])>0:
                ans += 1
                node = dic[node][0][0]
        return ans

        
            