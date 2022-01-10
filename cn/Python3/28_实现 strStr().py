# @algorithm @lc id=28 lang=python3 
# @title implement-strstr


from cn.Python3.mod.preImport import *
# @test("hello","ll")=2
# @test("aaaaa","bba")=-1
# @test("","")=0
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        def getNxt(x):
            # 从长到短遍历
            for i in range(x,0,-1):
                if needle[0:i] == needle[x-i+1:x+1]:
                    return i
            return 0
        nxt = [getNxt(x) for x in range(len(needle))]
        tar = 0
        pos = 0
        while tar<len(haystack):
            if haystack[tar] == needle[pos]:
                tar+=1
                pos+=1
            elif pos:
                pos = nxt[pos-1]
            else:
                tar += 1
            if pos == len(needle):
                return (tar-pos)
                pos = nxt[pos-1]
        return -1

