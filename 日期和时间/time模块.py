import time

# time函数用于返回当前时间的时间戳
print("当前事件的时间戳是：%f" % (time.time()))

# localtime函数的作用是将事件戳格式化为本地时间，返回struct_time对象，
# localtime函数有一个参数用于接收时间戳，如果不提供则会默认使用当前的时间戳
print("当前时间：", time.localtime())
print("0事件戳对应的(北京)时间：", time.localtime(0))

# mktime函数与gmtime、localtime函数相反的操作，它接收stuct_time对象作为参数，
# 返回用秒数来表示事件的浮点数。mktime的参数可以是结构化的时间，也可以是完整的9位元祖元素
t = (2018, 6, 18, 17, 3, 1, 1, 1, 0)
secs = time.mktime(t)
print("time.mktime(t):%f" % secs)
print("time.localtime(secs):", time.localtime(secs))
print("time.mktime(time.localtime(secs)):%f" % time.mktime(
    time.localtime(secs)))  # mktime可以使用元祖作为参数，也可以使用time_struct实例作为参数

# gmtime函数能将一个时间戳转换为UTC时区(0时区)的struct_time，可选的参数sec表示从1970-1-1以来的秒数
# gmtime函数的默认值为time.time()，函数返回time.struct_time类型的对象

print("time.gmtime():", time.gmtime())
print("time.gmtime(0):", time.gmtime(0))

# asctime函数接受事件元祖并返回一个可读形式为"Tue Jul 17 17:03:01 2018"(2018年7月17日周二17时03分01秒)的24个字符的字符串
# asctime函数接收的参数可以使9个元素的元祖，也可以是是通过函数gmtime()或localtime()返回的时间值(time_struct类型)
t = (2022, 10, 15, 16, 40, 1, 1, 1, 0)
print("time.asctime(t):", time.asctime(t))
print("time.asctime(time.localtime()):", time.asctime(time.localtime()))

# ctime函数能把一个实践出欧转化为time.asctime()的形式，默认参数为time.time()
# 相当于执行 asctime(localtime(secs))
print(time.ctime())

# sleep函数推迟调用线程得到运行，可以通过参数secs指定秒数
print("Start : %s" % time.ctime())
time.sleep(3)
print("End : %s" % time.ctime())

# strftime函数用于接收时间元祖，并返回以可读字符串表示的当地时间，格式由参数format决定
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# strptime函数能够根据指定的格式把一个时间字符串解析为时间元组(time_struct对象)
# 和strftime函数刚好相反
struct_time = time.strptime("2022-10-15 16:58:11", "%Y-%m-%d %H:%M:%S")
print("返回的元祖：", struct_time)
