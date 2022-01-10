# @algorithm @lc id=419 lang=python3 
# @title battleships-in-a-board


from cn.Python3.mod.preImport import *
# @test([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])=2
# @test([["."]])=0
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        import collections
        ans = 0
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    queue = collections.deque([(i,j)])
                    visited = [(i,j)]
                    ans += 1
                    while queue:
                        node_x,node_y = queue.popleft()
                        board[node_x][node_y] = '.'
                        for x,y in [(node_x-1,node_y),(node_x+1,node_y),(node_x,node_y-1),(node_x,node_y+1)]:
                            if 0<=x<m and 0<=y<n and (x,y) not in visited and board[x][y] == 'X':
                                queue.append((x,y))
                                visited.append((x,y))
        return ans

