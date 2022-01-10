# @algorithm @lc id=438 lang=python3 
# @title find-all-anagrams-in-a-string


from cn.Python3.mod.preImport import *
# @test("cbaebabacd","abc")=[0,6]
# @test("abab","ab")=[0,1,2]
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        import collections
        ans = []
        c2 = collections.Counter(p)
        for i in range(len(s) - len(p)+1):
            s_ = s[i:i+len(p)]
            c1 = collections.Counter(s_)
            if c1 == c2:
                ans.append(i)
        return ans
