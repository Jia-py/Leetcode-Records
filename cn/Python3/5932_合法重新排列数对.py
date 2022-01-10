# @algorithm @lc id=2201 lang=python3 weekname=weekly-contest-270
# @title valid-arrangement-of-pairs


from cn.Python3.mod.preImport import *
# @test([[5,1],[4,5],[11,9],[9,4]])=[[11,9],[9,4],[4,5],[5,1]]
# @test([[1,3],[3,2],[2,1]])=[[1,3],[3,2],[2,1]]
# @test([[1,2],[1,3],[2,1]])=[[1,2],[2,1],[1,3]]
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        dic = {}
        for index,i in enumerate(pairs):
            for j in range(2):
                if i[j] not in dic:
                    dic[i[j]] = (0,j,index)
                dic[i[j]][0] += 1
        head_index = 0
        tail_index = 0
        for key in dic:
            if dic[key][0] % 2 == 1:
                if dic[key][1] == 0:
                    head_index = dic[key][2]
                elif dic[key][1] == 1:
                    tail_index = dic[key][2]
        ans = []
        ans.append(pairs[head_index])
        pairs.remove(pairs[head_index])
        while pairs:
            pivot = ans[-1][1]
            


