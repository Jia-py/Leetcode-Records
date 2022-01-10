# @algorithm @lc id=1824 lang=python3 
# @title maximum-number-of-eaten-apples


from cn.Python3.mod.preImport import *
# @test([1,2,3,5,2],[3,2,1,4,2])=7
# @test([3,0,0,0,0,2],[3,0,0,0,0,2])=5
# @test([2,1,10],[2,10,1])=4

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq
        ans = 0
        q = []
        # 最大值，帮助确定天数范围
        max_ = max([max(apples),max(days)])
        for i in range(len(apples)+max_):
            if i < len(apples):
                # 入队
                heapq.heappush(q,(i+days[i],apples[i]))
            while q:
                # 不断出队，直到出现腐烂天数在当前天数之后，且苹果数大于0的
                node_day,node_apple = heapq.heappop(q)
                if node_day > i and node_apple > 0:
                    ans += 1
                    node_apple -= 1
                    if node_apple > 0:
                        heapq.heappush(q,(node_day,node_apple))
                    break
        return ans
            



            

        