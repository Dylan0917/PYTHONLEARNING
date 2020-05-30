# -*- coding: UTF-8 -*-
'''
使用键值对存储，具有极快的查找速度

key的特性
1.字典中的key必须唯一
key必须不可变对象
字符串整数可以作为key
list可变 不能作为key
字典是无顺序的
查找速度极其快
需要占用大量内存 内存浪费严重
'''
dict1 = {"tom":60,"lilei":80}
# 获取数据
print(dict1["tom"])
ret = dict1.get("ti")
if ret == None:
    print("有")
dict1["k1"] = 38
dict1["k1"] = 89
print(dict1) #{'tom': 60, 'lilei': 80, 'k1': 89}


#遍历
for key in dict1:
    print(key,dict1[key])

for value in dict1.values():
    print(value)
for k,v in dict1.items():
    print(key,value)

for i,v2 in enumerate(dict1):
    print(i,v2)