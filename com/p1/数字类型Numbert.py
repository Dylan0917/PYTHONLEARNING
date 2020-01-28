# 导入库
import math
import random
# python可以处理任意大小的整型数据
num1 = 10
num2 = num1
# 交互式赋值定义变量
num6, num7 = 6, 7
print(num6, num7)

# 浮点数：浮点型由整数部分与小数部分组成，浮点数运算可能会有四舍五入的误差
f1 = 1.1
f2 = 2.2
print(f1 + f2)

# 复数：实数部分和虚数部分组成

# 数字类型转换
print(int(1.9))
print(float(1))
print(int("3343"))
print(float("12.3"))
print("--------------------------")
# 数学函数
i1 = -10
print(abs(i1))  # 绝对值
print(10 > 9)  # 结果为True
print((9 > 2) - (6 < 1))  # 1
print(max(2, 6, 3, 2, 6, 7, 8, 9))
print(min(2, 6, 3, 2, 6, 7, 8, 9))

print(pow(2, 5))  # 2^5
print(round(1.526))  # round()四舍五入 2
print(round(1.526, 2))  # round()四舍五入 1.53

print(math.ceil(18.1))  # 向上取整 19
print(math.ceil(18.9))  # 向上取整 19

print(math.floor(18.1))  # 18
print(math.floor(18.9))  # 18

# 返回整数部分和小数部分
print(math.modf(22.3))   # (0.3000000000000007, 22.0)

print(math.sqrt(16))   # 开平方 4.0

# 随机数
print(random.choice([1, 2, 3, 4, 6, 8, 6]))

print(random.choice(range(5)))
# 产生一个1到100的随机数
r1 = range(100)
print(random.choice(r1) + 1)

# 方法返回指定递增基数集合中的一个随机数，基数默认值为1。
# random.randrange ([start,] stop [,step])
# start -- 指定范围内的开始值，包含在范围内。
# stop -- 指定范围内的结束值，不包含在范围内。
# step -- 指定递增基数。
print(random.randrange(1, 100, 3))
print(random.randrange(100))  # 0-99随机数

print(random.random())  # [0.1) 随机数

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
# shuffle() 方法将序列的所有元素随机排序
random.shuffle(list)
print(list)

# 随机生成一个实数 [3,9]
print(random.uniform(3, 9))






