# @algorithm @lc id=783 lang=python3 
# @title search-in-a-binary-search-tree


from cn.Python3.mod.preImport import *
# @test([4,2,7,1,3],2)=[2,1,3]
# @test([4,2,7,1,3],5)=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        ans_left = self.searchBST(root.left, val)
        ans_right = self.searchBST(root.right, val)
        if ans_left:
            return ans_left
        elif ans_right:
            return ans_right
        else:
            return