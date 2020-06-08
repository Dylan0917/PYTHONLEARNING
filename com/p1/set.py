# -*- coding: UTF-8 -*-
# 无序
s1 = set([1,2,3,4])
print(s1)

s2 = set({1,2,3,4})
print(s2)

s3 = set((1,2,3,4))
print(s3)

s4 = set({1:"dfdf",2:"dfedc",3:"wscv",4:"vbnmj"})
print(s4)

s1.add(7)
print(s1)

# s3.add({8})
# print(s3)

s1.update([9])
print(s1)
s1.update("yu")
print(s1)  #{1, 2, 3, 4, 7, 9, 'y', 'u'}

# for i in s1:
#     print(i)

# 交集
# 并集