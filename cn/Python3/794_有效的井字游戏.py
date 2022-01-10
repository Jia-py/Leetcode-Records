# @algorithm @lc id=810 lang=python3 
# @title valid-tic-tac-toe-state


from typing import Counter
from cn.Python3.mod.preImport import *
# @test(["O  ","   ","   "])=false
# @test(["XOX"," X ","   "])=false
# @test(["XXX","   ","OOO"])=false
# @test(["XOX","O O","XOX"])=true
# @test(["XXX","XOO","OO "])=false
# @test(["XXX","OOX","OOX"])=true
# @test(["OXX","XOX","OXO"])=false
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        counter = Counter(board[0]) + Counter(board[1]) + Counter(board[2])
        if not counter['O']<=counter['X']<=counter['O'] + 1:
            return False
        times_x = self.count_(board,'X')
        times_o = self.count_(board,'O')
        if times_x and times_o:
            return False
        if times_x and (counter['X'] == counter['O']):
            return False
        if times_o and (counter['X'] > counter['O']):
            return False
        return True
    
    def count_(self,board,character):
        ans = 0
        if board[0][0] == board[0][1] == board[0][2] == character: ans += 1
        if board[1][0] == board[1][1] == board[1][2] == character: ans += 1
        if board[2][0] == board[2][1] == board[2][2] == character: ans += 1
        if board[0][0] == board[1][0] == board[2][0] == character: ans += 1
        if board[0][1] == board[1][1] == board[2][1] == character: ans += 1
        if board[0][2] == board[1][2] == board[2][2] == character: ans += 1
        if board[0][0] == board[1][1] == board[2][2] == character: ans += 1
        if board[0][2] == board[1][1] == board[2][0] == character: ans += 1
        return ans