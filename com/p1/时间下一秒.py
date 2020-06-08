# -*- coding: UTF-8 -*-
timeStr = input()
timeList = timeStr.split(":")
# timeList = timeStr.split(":")
h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])

if s == 1:
    print("fdfd")

print("%d:%d:%d" %(h,m,s))