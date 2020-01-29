num = int(input("输入num"))
if num % 2 == 0:
    print("是偶数")
else:
    print("不是偶数")

# 水仙花数

num1 = int(input("水仙花判断： "))
if num1 > 999 or num1 < 100:
    print("不是水仙花数")
# g = num1 % 10
# s = (num1 - g) // 10 % 10
# b = (num1 - g - s * 10) // 100
g = num1 % 10
s = (num1 // 10) % 10
b = num1 // 100
if g ** 3 + s ** 3 + b ** 3 == num1:
    print("是水仙花")
else:
    print("不是水仙花数")


#  回文
num2 = int(input("回文数"))
s = num2
y = 0
while s > 0:
    y = y * 10 + s % 10
    s = s // 10
if y == num2:
    print("回文数")
else:
    print("不是回文数")

#  输入三个数 输出最大的值

num3 = int(input("第一个数字: "))
num4 = int(input("第二个数字: "))
num5 = int(input("第三个数字: "))

if num3 > num4:
    if num3 > num5:
        print(num3)
    else:
        print(num5)
else:
    if num4 > num5:
        print(num4)
    else:
        print(num5)
# --------------------------------------------------------
#         位运算符
# 按位与
print(5 & 7)
# 按位或
print(5 | 7)
# 按位异或
print(5 ^ 7)
# 按位取反
print(~5)


