# @algorithm @lc id=2235 lang=python3 weekname=biweekly-contest-69
# @title capitalize-the-title


from cn.Python3.mod.preImport import *
# @test("capiTalIze tHe titLe")="Capitalize The Title"
# @test("First leTTeR of EACH Word")="First Letter of Each Word"
# @test("i lOve leetcode")="i Love Leetcode"
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        str = title.split(' ')
        ans = []
        for i in str:
            if len(i) > 2:
                ans.append(i.capitalize())
                ans.append(' ')
            else:
                ans.append(i.lower())
                ans.append(' ')
        ans.pop(-1)
        return ''.join(ans)
