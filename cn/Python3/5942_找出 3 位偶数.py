# @algorithm @lc id=2215 lang=python3 weekname=weekly-contest-270
# @title finding-3-digit-even-numbers


from cn.Python3.mod.preImport import *
# @test([2,1,3,0])=[102,120,130,132,210,230,302,310,312,320]
# @test([2,2,8,8,2])=[222,228,282,288,822,828,882]
# @test([3,7,5])=[]
# @test([0,2,0,0])=[200]
# @test([0,0,0])=[]
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        for index1 in range(len(digits)):
            for index2 in range(len(digits)):
                for index3 in range(len(digits)):
                    if index1 != index2 and index2 != index3 and index1 != index3:
                        number = digits[index1]*100+digits[index2]*10+digits[index3]
                        if number >= 100 and number %2 ==0:
                            ans.append(number)
        ans = list(set(ans))
        ans = sorted(ans)
        return ans

