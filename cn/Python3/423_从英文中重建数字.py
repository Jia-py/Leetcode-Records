# @algorithm @lc id=423 lang=python3 
# @title reconstruct-original-digits-from-english


from cn.Python3.mod.preImport import *
# @test("owoztneoer")="012"
# @test("fviefuro")="45"
class Solution:
    def originalDigits(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        lis = {}
        def dec(character, word, number):
            nonlocal lis
            count = counter[character]
            lis[number] = count
            for j in word:
                counter[j] -= count
        dec('z','zero',0)
        dec('x','six',6)
        dec('w','two',2)
        dec('u','four',4)
        dec('r','three',3)
        dec('o','one',1)
        dec('s','seven',7)
        dec('v','five',5)
        dec('g','eight',8)
        dec('i','nine',9)
        ans = ''
        for i in range(10):
            ans += lis[i]*str(i)
        return ans
