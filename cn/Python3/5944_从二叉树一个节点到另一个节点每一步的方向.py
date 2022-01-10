# @algorithm @lc id=2217 lang=python3 weekname=weekly-contest-270
# @title step-by-step-directions-from-a-binary-tree-node-to-another


from cn.Python3.mod.preImport import *
# @test([5,1,2,3,null,6,4],3,6)="UURL"
# @test([2,1],2,1)="L"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(cur, startValue, destValue, stack):
                if not cur:
                    return
                if cur.val == startValue:
                    nonlocal path_start
                    path_start = stack.copy()
                    print(path_start)
                if cur.val == destValue:
                    nonlocal path_end
                    path_end = stack.copy()
                stack.append('L')
                dfs(cur.left, startValue, destValue, stack)
                stack.pop()
                stack.append('R')
                dfs(cur.right,startValue, destValue, stack)
                stack.pop()
        path_start,path_end = [],[]
        stack = []
        dfs(root,startValue,destValue,stack)
        print(path_start,path_end)
        index_range = min(len(path_end),len(path_start))
        equal_length = 0
        for i in range(index_range):
            if path_start[i] == path_end[i]:
                equal_length += 1
            else:
                break
        path_start = path_start[equal_length:]
        path_end = path_end[equal_length:]
        path_start = list(map(lambda x:'U',path_start))
        path_start.extend(path_end)
        ans = path_start
        return ''.join(ans)
