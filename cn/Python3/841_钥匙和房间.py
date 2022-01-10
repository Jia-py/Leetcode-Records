# @algorithm @lc id=871 lang=python3 
# @title keys-and-rooms


from cn.Python3.mod.preImport import *
# @test([[1],[2],[3],[]])=true
# @test([[1,3],[3,0,1],[2],[0]])=false
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = []
        def dfs(x):
            stack.append(x)
            nonlocal num
            num += 1
            for it in rooms[x]:
                if it not in stack:
                    dfs(it)
        num = 0
        dfs(0)
        return num == len(rooms)
