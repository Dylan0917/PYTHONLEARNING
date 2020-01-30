# 长度已经固定
list = [1, 2, "rerere", True]
print(list)
print(list[3])
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 + list2)  # [1, 2, 3, 1, 2, 3]
print(list1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(1 in list1)
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list3[2:5])   # [3, 4, 5]
print(list3[3:])   # [4, 5, 6, 7, 8, 9]
print(list3[:5])   # [1, 2, 3, 4, 5]
list4 = [1, 2, 3, 4, 5]
list4.append(6)
print(list4)
list4.append([7, 8])  # 追加一个元素
print(list4)
list5 = [1, 2, 3, 4, 5]
list5.extend([7, 8])  # 追加多个元素
print(list5)
list6 = [1, 2, 3, 4, 5]
list6.insert(0, 123)  # [123, 1, 2, 3, 4, 5]
print(list6)
list6 = [1, 2, 3, 4, 5]
print(list6.pop())  # 5  移除并输出
print(list6.pop(2))  # 3
print(list6.pop(-1))

list7 = [1, 2, 3, 4, 5]
list7.remove(1)  # 移除元素内容
print(list7)

list8 = [1, 2, 3, 4, 5]
print(list8.index(3))  # 2 找到第一个匹配的索引值
print(list8.index(3, 0, 3))  # 加一个范围
print(len(list8))  # 5
print(max(list8))  # 5 最大数

print(min(list8))  # 1 最小值
print(list8.count(3))  # 1 查看元素中出现的次数





