# @algorithm @lc id=2205 lang=python3 weekname=biweekly-contest-67
# @title find-good-days-to-rob-the-bank


from cn.Python3.mod.preImport import *
# @test([5,3,3,3,5,6,2],2)=[2,3]
# @test([1,1,1,1,1],0)=[0,1,2,3,4]
# @test([1,2,3,4,5,6],2)=[]
# @test([1],5)=[]
# @test([1,2,3,4], 1)=[]
# @test([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8], 2)=[5,10,14]
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if len(security) < time*2 + 1:
            return []
        if (time == 0):
            return [x for x in range(len(security))]
        # 前面窗口递增的个数
        o1 = 0
        # 后面窗口递减的个数
        o2 = 0
        # 初始化两个窗口的值
        for i in range(1,time+1):
            if (security[i]>security[i-1]): o1 += 1
        for i in range(time+1,2*time+1):
            if (security[i]<security[i-1]): o2 += 1
        print(o1,o2)
        # 移动窗口，更新o1,o2的值
        ans = []
        for i in range(time,len(security)-time):
            if i == time:
                if o1==o2==0: ans.append(i)
            else:
                if security[i-time] > security[i-time-1]: o1 -= 1
                if security[i] > security[i-1]: o1 += 1
                if security[i] < security[i-1]: o2 -= 1
                if security[i+time] < security[i+time-1]: o2 += 1
                if o1==o2==0: ans.append(i)
        return ans


            

