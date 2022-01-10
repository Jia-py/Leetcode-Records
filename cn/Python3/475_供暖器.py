# @algorithm @lc id=475 lang=python3 
# @title heaters


from cn.Python3.mod.preImport import *
# @test([1,2,3],[2])=1
# @test([1,2,3,4],[1,4])=1
# @test([1,5],[2])=3
# @test([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923], [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])=161834419
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        import bisect
        heaters = sorted(heaters)
        ans = []
        for house in houses:
            index = bisect.bisect_left(heaters,house)
            if index == 0:
                ans.append(abs(house-heaters[index]))
            elif index == len(heaters):
                ans.append(abs(house-heaters[index-1]))
            else:
                dis1 = abs(house-heaters[index])
                dis2 = abs(house-heaters[index-1])
                ans.append(min([dis1,dis2]))
        return max(ans)
