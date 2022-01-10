# @algorithm @lc id=56 lang=python3 
# @title merge-intervals


from cn.Python3.mod.preImport import *
# @test([[1,3],[2,6],[8,10],[15,18]])=[[1,6],[8,10],[15,18]]
# @test([[1,4],[4,5]])=[[1,5]]
# @test([[1,4],[0,2],[3,5]])=[[0,5]]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        lis = sorted(intervals)
        for i in range(len(lis)-1):
            if lis[i][1] >= lis[i+1][0]:
                if lis[i][1] >= lis[i+1][1]:
                    lis[i+1] = [lis[i][0],lis[i][1]]
                else:
                    lis[i+1] = [lis[i][0],lis[i+1][1]]
                lis[i] = 0
        while 0 in lis:
            lis.remove(0)
        return lis