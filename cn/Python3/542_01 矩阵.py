# @algorithm @lc id=542 lang=python3 
# @title 01-matrix


from typing import Collection
from cn.Python3.mod.preImport import *
# @test([[0,0,0],[0,1,0],[0,0,0]])=[[0,0,0],[0,1,0],[0,0,0]]
# @test([[0,0,0],[0,1,0],[1,1,1]])=[[0,0,0],[0,1,0],[1,2,1]]
# @test([[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]])=[[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
# @test([[0,0,0],[0,1,0],[1,1,1]])=[[0,0,0],[0,1,0],[1,2,1]]
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        import collections
        m,n = len(mat),len(mat[0])
        dist = [[0]*n for _ in range(m)]
        zeroes_pos = [(i,j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)

        while q:
            i,j=q.popleft()
            for ni,nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=ni<m and 0<=nj<n and (ni,nj) not in seen:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni,nj))
                    seen.add((ni,nj))
        return dist
        # bfs(time out)
        # import collections
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 1:
        #             mat[i][j] = 999
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 0:
        #             queue = collections.deque([(i,j,0)])
        #             visited = [(i,j)]
        #             while queue:
        #                 x,y,distance = queue.popleft()
        #                 for x_,y_ in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        #                     if 0<=x_<len(mat) and 0<=y_<len(mat[0]) and (x_,y_) not in visited:
        #                         queue.append((x_,y_,distance+1))
        #                         if mat[x_][y_] != 0:
        #                             if distance + 1 < mat[x_][y_]:
        #                                 mat[x_][y_] = distance + 1
        #                         visited.append((x_,y_))
        # return mat

