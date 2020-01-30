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

list8.reverse()  # 翻转
print(list8)
list9 = [5, 6, 2, 1, 4, 8, 9]
list9.sort()  # 升序
print(list9)

# 浅拷贝 引用拷贝
list10 = [5, 6, 2, 1, 4, 8, 9]
list11 = list10
list10[1] = 300
print(list11)  # [5, 300, 2, 1, 4, 8, 9]

# 深拷贝
list12 = [5, 6, 2, 1, 4, 8, 9]
list13 = list12.copy()
print(id(list12))
print(id(list13))
list12[1] = 300
print(list13)  # [5, 6, 2, 1, 4, 8, 9]

# 将元组转成列表

# 分解质因数
# 对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,
# 　重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
num = int(input("分解质因数： "))
i = 2
while num != 1:
    if num % i == 0:
        print(i)
        num //= i
    else:
        i += 1
