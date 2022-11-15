import datetime

"""
    datetime模块包含了日期和时间的所有信息，支持从0001到9999年之间的日期
    datetime模块内定义了两个常量最小年份1和最大面粉9999
"""

"""
    date对象表示在日历中的一个日期（包含年月日），date对象的构造函数需要传入三个参数，year,month,day三个参数必须是有效的，真实存在的天数
"""

# today函数返回当天日期
today = datetime.date.today();
print("今天是：",today)

# weekday方法返回当前星期数，0~6
# isoweekday方法返回的是从1~7
print("weekday:",today.weekday())
print("isoweekday:",today.isoweekday())

# isoformat方法返回日期为ISO格式，即"YYYY-MM-DD"的字符串
date = datetime.date(2022,10,15)
print(date.isoformat()) # 直接输出date调用的就是isoformat方法

# strftime方法可以格式化输出日期
print(date.strftime("%Y/%m/%d"))
print(date.strftime("%y %b %d"))


