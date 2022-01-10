# @algorithm @lc id=2228 lang=python3 weekname=weekly-contest-271
# @title watering-plants-ii


from cn.Python3.mod.preImport import *
# @test([2,2,3,3],5,5)=1
# @test([2,2,3,3],3,4)=2
# @test([5],10,8)=0
# @test([1,2,4,4,5],6,5)=2
# @test([2,2,5,2,2],5,5)=1
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alice = 0
        bob = len(plants)-1
        ans = 0
        alice_water = capacityA
        bob_water = capacityB
        while alice < bob:
            if plants[alice] > alice_water:
                alice_water = capacityA
                ans += 1
                alice_water = alice_water - plants[alice]
                alice += 1
            else:
                alice_water = alice_water - plants[alice]
                alice += 1
            if plants[bob] > bob_water:
                bob_water = capacityB
                ans += 1
                bob_water = bob_water - plants[bob]
                bob -= 1
            else:
                bob_water = bob_water - plants[bob]
                bob -= 1
        if alice == bob:
            if alice_water >= bob_water:
                if plants[alice] > alice_water:
                    ans += 1
            else:
                if plants[alice] > bob_water:
                    ans += 1
        return ans

