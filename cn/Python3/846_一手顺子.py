# @algorithm @lc id=876 lang=python3 
# @title hand-of-straights


from cn.Python3.mod.preImport import *
# @test([1,2,3,6,2,3,4,7,8],3)=true
# @test([1,2,3,4,5],4)=false
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        import collections
        counter = collections.Counter(hand)
        hand = sorted(hand)
        while hand:
            node = hand[0]
            for i in range(groupSize):
                if counter[node+i] < 1:
                    return False
                counter[node+i] -= 1
                hand.remove(node+i)
        return True
