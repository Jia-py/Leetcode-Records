# @algorithm @lc id=89 lang=python3 
# @title gray-code


from cn.Python3.mod.preImport import *
# @test(2)=[0,1,3,2]
# @test(1)=[0,1]
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n+1):
            for j in range(len(ans)-1,-1,-1):
                ans.append(ans[j] | (1<<i-1))
        return ans