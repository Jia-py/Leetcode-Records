# @algorithm @lc id=5 lang=python3 
# @title longest-palindromic-substring


from cn.Python3.mod.preImport import *
# @test("babad")="bab"
# @test("cbbd")="bb"
# @test("a")="a"
# @test("ac")="a"
# @test("aacabdkacaa")="aca"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        ans = []
        for index in range(len(s)-1):
            # 当前元素存入数组
            tmp = [s[index]]
            i = index - 1
            # 向左拓展找与s[index]相同的元素
            while  0<=i<len(s):
                if s[i] == s[index]:
                    tmp.insert(0,s[i])
                    i -= 1
                else:
                    break
            # 向右扩展
            j = index + 1
            while 0<=j<len(s):
                if s[j] == s[index]:
                    tmp.append(s[j])
                    j += 1
                else:
                    break
            # 向两边扩展
            while 0<=i<len(s) and 0<=j<len(s):
                if s[i] == s[j]:
                    tmp.insert(0,s[i])
                    tmp.append(s[i])
                    i -= 1
                    j += 1
                else:
                    break
            if len(tmp) > len(ans):
                ans = tmp
        return ''.join(ans)

