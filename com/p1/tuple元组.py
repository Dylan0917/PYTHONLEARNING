tuple1 = (1, 2, 3, 4, "good", True)
print(tuple1)
tuple2 = (1, )
print(tuple2)
print(type(tuple2))

# 元素访问 [下标]
tuple4 = (1, 2, 3, 4)
print(tuple4[0])
print(tuple4[-1])  # 最后一个元素
print(tuple4[-2])

# 元组一旦初始化就不能被修改
# 删除元组
tuple5 = (1, 2, 3, 4, 5)
del tuple5

# 元组操作
tuple6 = (1, 2, 3)
tuple7 = (4, 5, 6)
print(tuple6 + tuple7)

# 元组重复
print(tuple6 * 2)

# 是否存在元素
print(4 in tuple6)

# 元组的截取
tuple8 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple8[3:])

# 二维元组
# 元组的方法
tuple9 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 元素的个数
print(len(tuple9))
print(max(tuple9))
print(min(tuple9))
print(tuple([1, 2, 3]))
# 元组的遍历
for i in tuple9:
    print(i)
# 元组不可变 列表可变
