# @algorithm @lc id=71 lang=python3 
# @title simplify-path


from cn.Python3.mod.preImport import *
# @test("/home/")="/home"
# @test("/../")="/"
# @test("/home//foo/")="/home/foo"
class Solution:
    def simplifyPath(self, path: str) -> str:
        # lis = []
        # for i in range(len(path)):
        #     if i == 0:
        #         lis.append(path[i])
        #         continue
        #     else:
        #         if path[i] == '/' and path[i-1] == '/':
        #             continue
        #         else:
        #             lis.append(path[i])
        path = path.split('/')
        lis = []
        for i in path:
            if i != '':
                lis.append(i)
        stack = []
        for i in lis:
            if i == '.':
                continue
            elif i == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop(-1)
            else:
                stack.append(i)
        if len(stack) == 0:
            return '/'
        else:
            ans = ''
            for i in stack:
                ans += '/' + str(i)
            return ans