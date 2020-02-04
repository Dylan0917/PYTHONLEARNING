for i in [1, 2, 3]:
    print(i)
# range() 列表生成器
for x in range(10):
    print(x)

for y in range(2, 20, 2):
    print(y)

# 同时便利下标和元素
for index, m in enumerate([1, 2, 3]):
    print(index, m)

# 打印99乘法表
# h = 1
for h in range(1, 10):
    for l in range(1, h + 1):
        print("%d * %d = %d" % (h, l, h*l))

# 求俩数字的最大公约数


# 随机生成6位数的验证码