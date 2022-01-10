# @algorithm @lc id=2191 lang=python3 weekname=biweekly-contest-66
# @title minimum-number-of-buckets-required-to-collect-rainwater-from-houses


from cn.Python3.mod.preImport import *
# @test("H..H")=2
# @test(".H.H.")=1
# @test(".HHH.")=-1
# @test("H")=-1
# @test(".")=0
class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        s = set()
        
        for i, ch in enumerate(street):
            if ch == 'H':
                if i - 1 in s:
                    continue
                if i + 1 < n and street[i + 1] == '.':
                    s.add(i + 1)
                elif i >= 1 and street[i - 1] == '.':
                    s.add(i - 1)
                else:
                    return -1
                    
        return len(s)
