# @algorithm @lc id=2239 lang=python3 weekname=weekly-contest-273
# @title execution-of-all-suffix-instructions-staying-in-a-grid


from cn.Python3.mod.preImport import *
# @test(3,[0,1],"RRDDLU")=[1,5,4,3,1,0]
# @test(2,[1,1],"LURD")=[4,1,0,0]
# @test(1,[0,0],"LRUD")=[0,0,0,0]
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        ini_pos = startPos.copy()
        for i in range(len(s)):
            path = s[i:]
            step = 0
            startPos = ini_pos.copy()
            for j in path:
                if j=='R':
                    if startPos[1] + 1 > n-1:
                        ans.append(step)
                        break
                    else:
                        startPos[1] += 1
                        step += 1
                elif j == 'L':
                    if startPos[1] - 1 < 0:
                        ans.append(step)
                        break
                    else:
                        startPos[1] -= 1
                        step += 1
                elif j == 'U':
                    if startPos[0] - 1 <0:
                        ans.append(step)
                        break
                    else:
                        startPos[0] -= 1
                        step += 1
                elif j == 'D':
                    if startPos[0] + 1 > n-1:
                        ans.append(step)
                        break
                    else:
                        startPos[0] += 1
                        step += 1
            if step == len(path):
                ans.append(step)
        return ans
