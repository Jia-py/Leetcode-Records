# @algorithm @lc id=1731 lang=python3 
# @title even-odd-tree


from collections import defaultdict
from cn.Python3.mod.preImport import *
# @test([1,10,4,3,null,7,9,12,8,6,null,null,2])=true
# @test([5,4,2,3,3,7])=false
# @test([5,9,1,3,5,7])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0
        while queue:
            prev = float('inf') if level%2==1 else 0
            # 下一层的数组
            nxt = []
            for node in queue:
                val = node.val
                if val % 2 == level % 2 or level % 2 == 0 and val <= prev or level % 2 == 1 and val >= prev:
                    return False
                prev = val
                # 一定要先左再右，保证顺序
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            level += 1
            queue = nxt
        return True