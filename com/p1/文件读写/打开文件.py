# -*- coding: UTF-8 -*-
'''
r 只读方式打开文件 文件对描述符放在文件对开头
rb 以二进制的格式打开一个文件用于只读，文件描述符放在文件的 开头
r+ 读写方式打开文件 文件对描述符放在文件对开头
w 只写方式打开文件 存在则覆盖不存在则新建
wb 打开一个文件用于写入二进制 存在则覆盖不存在则新建
w+ 打开文件用于读写
a 打开一个文件用于追加
a+

'''

f = open("/Users/ywh/CODESRC/pf","r")
# str1 = f.read()
# print(str1)
# 读取指定字符
# str2 = f.read(3)
# print(str2)
# str3 = f.readline()
# print(str3)
# print(f.readline())


str4 = f.readlines()
print(str4)

f.close()