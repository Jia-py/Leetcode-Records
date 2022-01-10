# @algorithm @lc id=383 lang=python3 
# @title ransom-note


from cn.Python3.mod.preImport import *
# @test("a","b")=false
# @test("aa","ab")=false
# @test("aa","aab")=true
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)
        for key in counter1:
            if counter1[key] > counter2[key]:
                return False
        return True