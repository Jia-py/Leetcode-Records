# @algorithm @lc id=2216 lang=python3 weekname=weekly-contest-270
# @title delete-the-middle-node-of-a-linked-list


from cn.Python3.mod.preImport import *
# @test([1,3,4,7,1,2,6])=[1,3,4,1,2,6]
# @test([1,2,3,4])=[1,2,4]
# @test([2,1])=[2]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        node = head
        while True:
            if node.next == None:
                break
            else:
                node = node.next
                length += 1
        zhong = int(length /2)
        node = head
        for i in range(zhong-1):
            node = node.next
        node.next = node.next.next
        return head