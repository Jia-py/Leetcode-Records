# @algorithm @lc id=2244 lang=python3 weekname=weekly-contest-274
# @title number-of-laser-beams-in-a-bank


from cn.Python3.mod.preImport import *
# @test(["011001","000000","010100","001000"])=8
# @test(["000","111","000"])=0
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        if m == 1:
            return 0
        n = len(bank[0])
        ans = 0
        lis = []
        for i in range(m):
            num = bank[i].count('1')
            lis.append(num)
        last = lis[0]
        for i in range(1,m):
            if lis[i] == 0 :
                continue
            else:
                ans += last * lis[i]
                last = lis[i]
        return ans
