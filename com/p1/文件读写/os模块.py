import os
import time
print(os.name)
# print(os.uname())
print(os.curdir)
# os.mkdir('yu')
# os.rmdir('yu')
# print(os.stat('yu'))

now = int(1501124501)
#转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
print(timeArray)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

# 删除普通文件
# os.remove("")

print(os.path.abspath("."))

# 拼接路径
p1 = "/fd"
p2 = "gsg/f"
print(os.path.join(p1,p2))
p3 = os.path.join(p1,p2)
print(os.path.split(p3))
print(os.path.splitext(p3))
print(os.path.isdir(p3))
print(os.path.isfile(p3))

print(os.path.exists(p3))

# print(os.path.getsize())