# @algorithm @lc id=749 lang=python3 
# @title shortest-completing-word


from typing import Counter
from cn.Python3.mod.preImport import *
# @test("1s3 PSt",["step","steps","stripe","stepple"])="steps"
# @test("1s3 456",["looks","pest","stew","show"])="pest"
# @test("Ah71752",["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])="husband"
# @test("OgEu755",["enough","these","play","wide","wonder","box","arrive","money","tax","thus"])="enough"
# @test("iMSlpe4",["claim","consumer","student","camera","public","never","wonder","simple","thought","use"])="simple"
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        dic = {}
        for i in licensePlate:
            if 'a'<=i<='z':
                if i not in dic:
                    dic[i] = 0
                dic[i] += 1
        ans = []
        for j in words:
            flag = True
            tmp_counter = Counter(j)
            for key in dic:
                if tmp_counter[key] < dic[key]:
                    flag = False
            if flag:
                ans.append(j)
        ans = sorted(ans,key=lambda x:len(x))
        return ans[0]
        
            
            