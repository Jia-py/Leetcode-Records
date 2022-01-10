# @algorithm @lc id=2236 lang=python3 weekname=biweekly-contest-69
# @title maximum-twin-sum-of-a-linked-list


from cn.Python3.mod.preImport import *
# @test([5,4,2,1])=6
# @test([4,2,2,3])=7
# @test([1,100000])=100001
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lis = []
        node = head
        while node:
            lis.append(node.val)
            node = node.next
        ans = 0
        for i in range(len(lis)//2):
            ans = max(ans,lis[i] + lis[len(lis)-1-i])
        return ans