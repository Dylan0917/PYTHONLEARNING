# -*- coding: UTF-8 -*-

'''
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
'''
print("---------------------------------------------")
try:
    print(3 / 0)
except ZeroDivisionError as e:
    print("除数为0")
print("---------------------------------------------")
try:
    print(3/0)
except BaseException as e:
    print(e)
finally:
    print("----finally")

def f1():
    try:
        print(2)
        return 1
    except BaseException as e:
        return 0
    finally:
        print("finally")
aa = f1()
print(aa)