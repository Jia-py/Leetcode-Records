# @algorithm @lc id=2192 lang=python3 weekname=biweekly-contest-66
# @title minimum-cost-homecoming-of-a-robot-in-a-grid


from cn.Python3.mod.preImport import *
# @test([1,0],[2,3],[5,4,3],[8,2,6,7])=18
# @test([0,0],[0,0],[5],[26])=0
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        import collections
        # m = len(rowCosts)
        # n = len(colCosts)
        # visited = {}
        # ans = 0
        # def dfs(cur_node, cost):
        #     nonlocal ans
        #     if cur_node == homePos:
        #         if cost < ans: ans = cost
        #     x_node = cur_node[0]
        #     y_node = cur_node[1]
        #     for x,y in [(x_node+1,y_node),(x_node-1,y_node),(x_node,y_node+1),(x_node,y_node-1)]:
        #         if 0<=x<m and 0<=y<n:
        #             if (x,y) not in visited:
        #                 # 走的是x
        #                 if x != x_node:
        #                     visited[(x,y)] = cost + rowCosts[x]
        #                     tmp = cost + rowCosts[x]
        #                 else:
        #                     visited[(x,y)] = cost + colCosts[y]
        #                     tmp = cost + colCosts[y]
        #                 dfs([x,y],tmp)
        #             else:
        #                 if x != x_node:
        #                     if visited[(x,y)] > cost + rowCosts[x]:
        #                         visited[(x,y)] = cost + rowCosts[x]
        #                         tmp = cost + rowCosts[x]
        #                         dfs([x,y],tmp)
        #                 else:
        #                     if visited[(x,y)] > cost + colCosts[y]:
        #                         visited[(x,y)] = cost + colCosts[y]
        #                         tmp = cost + colCosts[y]
        #                         dfs([x,y],tmp)
                    
        # dfs(startPos,0)
        # return ans

        ans = 0
        print(homePos[0])
        if homePos[0] < startPos[0]:
            for i in range(homePos[0],startPos[0]):
                ans += rowCosts[i]
        else:
            for i in range(homePos[0],startPos[0], -1):
                ans += rowCosts[i]
        if homePos[1] < startPos[1]:
            for j in range(homePos[1],startPos[1]):
                ans += colCosts[j]
        else:
            for j in range(homePos[1],startPos[1],-1):
                ans += colCosts[j]
        return ans

            
