# @algorithm @lc id=2231 lang=python3 weekname=weekly-contest-272
# @title find-first-palindromic-string-in-the-array


from cn.Python3.mod.preImport import *
# @test(["abc","car","ada","racecar","cool"])="ada"
# @test(["notapalindrome","racecar"])="racecar"
# @test(["def","ghi"])=""
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for str in words:
            if str == str[::-1]:
                return str
        return ""