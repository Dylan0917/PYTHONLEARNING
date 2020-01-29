"""
while 语句:
      语句
"""

i = 1
while i <= 1000:
    print(i)
    i += 1
i = 1
sum1 = 0
while i <= 100:
    sum1 += i
    i += 1
print("sum = %d" % sum1)

"""
打印出所有的三位数中的水仙花数
五位数中的回文数
从控制台输入一个数 判断是否是质数
从控制台输入一个数 分解质因数
"""
print("-------------练习-水仙花start------------------")
i = 100
while i <= 999:
    g = i % 10
    s = (i // 10) % 10
    b = i // 100
    if g ** 3 + s ** 3 + b ** 3 == i:
        print(i)
    i += 1
print("-------------练习-水仙花end------------------")
print("-------------练习-回文start------------------")
i = 10000
while i <= 99999:
    y = 0
    s = i
    while s > 0:
        y = y * 10 + s % 10
        s = s // 10
    if y == i:
        print(i)
    i += 1
print("-------------练习-回文end------------------")
print("-------------练习-质数start------------------")
zstest = 17
i = 2
if zstest == 1:
    print("不是质数")
if zstest == 2:
    print("是质数")
while i <= zstest-1:
    if zstest % i == 0:
        print("不是质数")
        break
    i += 1
if i == zstest:
    print("是质数")

print("-------------练习-质数end------------------")



