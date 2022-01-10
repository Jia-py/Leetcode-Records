# @algorithm @lc id=1104 lang=python3 
# @title coloring-a-border


from cn.Python3.mod.preImport import *
# @test([[1,1],[1,2]],0,0,3)=[[3,3],[3,2]]
# @test([[1,2,2],[2,3,2]],0,1,3)=[[1,3,3],[2,3,3]]
# @test([[1,1,1],[1,1,1],[1,1,1]],1,1,2)=[[2,2,2],[2,1,2],[2,2,2]]
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        from collections import deque
        queue = deque([(row,col)])
        visited = [(row,col)]
        m = len(grid)
        n = len(grid[0])
        value = grid[row][col]
        while queue:
            node = queue.popleft()
            if node[0] == 0 or node[0] == m-1 or node[1] == 0 or node[1] == n -1:
                grid[node[0]][node[1]] = color
            for x,y in [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]-1),(node[0],node[1]+1)]:
                if 0<=x<m and 0<=y<n and (x,y) not in visited:
                    if grid[x][y] != value:
                        grid[node[0]][node[1]] = color
                    else:
                        queue.append((x,y))
                        visited.append((x,y))
        return grid

