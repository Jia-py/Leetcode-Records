# @algorithm @lc id=1944 lang=python3 
# @title truncate-sentence


from cn.Python3.mod.preImport import *
# @test("Hello how are you Contestant",4)="Hello how are you"
# @test("What is the solution to this problem",4)="What is the solution"
# @test("chopper is not a tanuki",5)="chopper is not a tanuki"
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lis = s.split(' ')
        print(lis)
        if len(lis) == k:
            return s
        ans = ''
        for i in range(k-1):
            ans = ans + lis[i] + ' '
        ans = ans + lis[k-1]
        return ans
