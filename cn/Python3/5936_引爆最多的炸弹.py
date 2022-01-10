# @algorithm @lc id=2206 lang=python3 weekname=biweekly-contest-67
# @title detonate-the-maximum-bombs


from typing import Collection
from cn.Python3.mod.preImport import *
# @test([[2,1,3],[6,1,4]])=2
# @test([[1,1,5],[10,10,5]])=1
# @test([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])=5
# @test([[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]])=1
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        import collections
        def distance(x1,y1,r1,x2,y2,r2):
            dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if dis <= r1:
                return True
            else:
                return False
        lis = []
        for i in range(len(bombs)):
            tmp = []
            for j in range(len(bombs)):
                if (i != j) and distance(bombs[i][0],bombs[i][1],bombs[i][2],bombs[j][0],bombs[j][1],bombs[j][2]):
                    tmp.append(j)
            lis.append(tmp)
        ans = []
        for i in range(len(bombs)):
            queue = collections.deque([i])
            visited = [i]
            while queue:
                node = queue.popleft()
                for j in lis[node]:
                    if j in visited:
                        continue
                    else:
                        queue.append(j)
                        visited.append(j)
            ans.append(len(visited))
        return max(ans)
                        

