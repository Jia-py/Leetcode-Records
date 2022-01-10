# @algorithm @lc id=852 lang=python3 
# @title friends-of-appropriate-ages


from cn.Python3.mod.preImport import *
# @test([16,16])=2
# @test([16,17,18])=2
# @test([20,30,100,110,120])=3
# @test([101,56,69,48,30])=4
# @test([54,23,102,90,40,74,112,74,76,21])=22
# @test([73,106,39,6,26,15,30,100,71,35,46,112,6,60,110])=29
# @test([81,106,11,66,83,113,51,62,47,42,85,94,78,96,51,14,3,111,57,66,8,113,27,61,21,55,87,15,20,23,14,105,38,85,2,108,103,46,44,27,79,108,106,86,113,24,39,8,7,97])=434
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        import collections
        counter = collections.Counter(ages)
        ans = 0
        # 计算自己和自己的
        for key in counter:
            if key <= 14: continue
            ans += counter[key]*(counter[key]-1)
        key = sorted(list(counter.keys()))
        for i in range(len(key)):
            # 保证ages[j] < ages[i]
            for j in range(i):
                if key[j]>0.5*key[i] + 7:
                    ans += counter[key[i]] * counter[key[j]]
        return ans
