# @algorithm @lc id=2240 lang=python3 weekname=weekly-contest-273
# @title intervals-between-identical-elements


from cn.Python3.mod.preImport import *
# @test([2,1,3,1,2,3,3])=[4,2,7,2,4,4,5]
# @test([10,5,10,10])=[5,0,3,4]
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        def func(array):
            dic = {}
            # 存储前缀后缀和的数组
            lis = []
            for i in range(len(array)):
                if array[i] not in dic:
                    dic[array[i]] = [[i],1]
                    lis.append(0)
                else:
                    dic[array[i]][0].append(i)
                    dic[array[i]][1] += 1
                    former_idx = dic[array[i]][0][-1]
                    former_num = dic[array[i]][1]-1
                    lis.append( (i-former_idx) * former_num + lis[former_idx])
            return lis
        prefix = func(arr)
        suffix = func(arr[::-1])
        ans = prefix + suffix
        return ans
                
