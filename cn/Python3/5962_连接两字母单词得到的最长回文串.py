# @algorithm @lc id=2237 lang=python3 weekname=biweekly-contest-69
# @title longest-palindrome-by-concatenating-two-letter-words


from cn.Python3.mod.preImport import *
# @test(["lc","cl","gg"])=6
# @test(["ab","ty","yt","lc","cl","ab"])=8
# @test(["cc","ll","xx"])=2
# @test(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"])=22
# @test(["em","pe","mp","ee","pp","me","ep","em","em","me"])=14
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        dic = {}
        for i in words:
            if i not in dic:
                dic[i] = [0,0]
            if i == i[::-1]:
                dic[i][1] = 1
            dic[i][0] += 1
        # 找到最多的奇数对称字符串
        max_num = 0
        max_key = None
        for key in dic:
            if dic[key][1] == 1 and dic[key][0] % 2 == 1 and dic[key][0] > max_num:
                max_num = dic[key][0]
                max_key = key
        for key in dic:
            if dic[key][1] == 1:
                if key == max_key:
                    ans += 2*dic[key][0]
                    dic[key][0] = 0
                else:
                    ans += 2*(dic[key][0]//2 * 2)
            else:
                if key[::-1] in dic:
                    num = min(dic[key][0],dic[key[::-1]][0])
                    ans += 4*num
                    dic[key][0] -= num
                    dic[key[::-1]][0] -= num
        return ans

            