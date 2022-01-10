# @algorithm @lc id=506 lang=python3 
# @title relative-ranks


from cn.Python3.mod.preImport import *
# @test([5,4,3,2,1])=["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# @test([10,3,8,9,4])=["Gold Medal","5","Bronze Medal","Silver Medal","4"]
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        index_sorted = sorted(range(len(score)),key=lambda k:score[k], reverse=True)
        for i in range(1,len(score)+1):
            if i == 1:
                score[index_sorted[i-1]] = 'Gold Medal'
            elif i == 2:
                score[index_sorted[i-1]] = 'Silver Medal'
            elif i == 3:
                score[index_sorted[i-1]] = 'Bronze Medal'
            else:
                score[index_sorted[i-1]] = str(i)
        return score