# @algorithm @lc id=802 lang=python3 
# @title k-th-smallest-prime-fraction


from cn.Python3.mod.preImport import *
# @test([1,2,3,5],3)=[2,5]
# @test([1,7],1)=[1,7]
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lis = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                lis.append([arr[i]/arr[j],arr[i],arr[j]])
        lis = sorted(lis)
        return [lis[k-1][1],lis[k-1][2]]