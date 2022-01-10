# @algorithm @lc id=1260 lang=python3 
# @title day-of-the-year


from cn.Python3.mod.preImport import *
# @test("2019-01-09")=9
# @test("2019-02-10")=41
# @test("2003-03-01")=60
# @test("2004-03-01")=61
class Solution:
    def dayOfYear(self, date: str) -> int:
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        import datetime
        time = datetime.datetime.strptime(date,'%Y-%m-%d')
        time2 = datetime.datetime.strptime(year+'-01-01','%Y-%m-%d')
        return (time-time2).days + 1
