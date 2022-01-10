# @algorithm @lc id=1156 lang=python3 
# @title occurrences-after-bigram


from cn.Python3.mod.preImport import *
# @test("alice is a good girl she is a good student","a","good")=["girl","student"]
# @test("we will we will rock you","we","will")=["we","rock"]
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        text = text.split()
        for i in range(2,len(text)):
            if text[i-2] == first and text[i-1] == second:
                ans.append(text[i])
        return ans