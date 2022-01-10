# @algorithm @lc id=2256 lang=python3 weekname=weekly-contest-275
# @title count-words-obtained-after-adding-a-letter


from collections import Counter
from cn.Python3.mod.preImport import *
# @test(["ant","act","tack"],["tack","act","acti"])=2
# @test(["ab","a"],["abc","abcd"])=1
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        a=set()
        for s in startWords:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c not in s:
                    a.add(''.join(sorted(s+c)))
        return sum(''.join(sorted(i)) in a for i in targetWords)