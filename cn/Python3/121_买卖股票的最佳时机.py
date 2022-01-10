# @algorithm @lc id=121 lang=python3 
# @title best-time-to-buy-and-sell-stock


from cn.Python3.mod.preImport import *
# @test([7,1,5,3,6,4])=5
# @test([7,6,4,3,1])=0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        暴力解 超时
        ans = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i] :
                    ans = max(ans,prices[j]-prices[i])
        return ans
        '''
        # 动态规划
        max_profit = 0
        min_price = 1e9
        for i in prices:
            min_price = min(min_price,i)
            max_profit = max(max_profit,i-min_price)
        return max_profit