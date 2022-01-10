# @algorithm @lc id=1737 lang=python3 
# @title maximum-nesting-depth-of-the-parentheses


from cn.Python3.mod.preImport import *
# @test("(1+(2*3)+((8)/4))+1")=3
# @test("(1)+((2))+(((3)))")=3
class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        max_depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop(-1)
                max_depth = max(max_depth,len(stack) + 1)
        return max_depth
