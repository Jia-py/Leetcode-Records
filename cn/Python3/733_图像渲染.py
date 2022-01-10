# @algorithm @lc id=733 lang=python3 
# @title flood-fill


from cn.Python3.mod.preImport import *
# @test([[1,1,1],[1,1,0],[1,0,1]],1,1,2)=[[2,2,2],[2,2,0],[2,0,1]]
# @test([[0,0,0],[0,0,0]],0,0,2)=[[2,2,2],[2,2,2]]
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        import collections
        m = len(image)
        n = len(image[0])
        queue = collections.deque([(sr,sc)])
        value = image[sr][sc]
        if value == newColor:
            return image
        else:
            image[sr][sc] = newColor
        while queue:
            x,y = queue.popleft()
            for new_x,new_y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<= new_x <m and 0<=new_y<n and image[new_x][new_y] == value:
                    queue.append((new_x,new_y))
                    image[new_x][new_y] = newColor
        return image