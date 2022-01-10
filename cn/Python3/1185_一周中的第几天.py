# @algorithm @lc id=1289 lang=python3 
# @title day-of-the-week


from cn.Python3.mod.preImport import *
# @test(31,8,2019)="Saturday"
# @test(18,7,1999)="Sunday"
# @test(15,8,1993)="Sunday"
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dic = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',
               5:'Friday',6:'Saturday',0:'Sunday'}
        week_num = int(datetime.datetime(year,month,day).strftime("%w"))
        return dic[week_num]