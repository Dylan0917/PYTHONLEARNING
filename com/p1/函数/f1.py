# -*- coding: UTF-8 -*-
# 函数就是对功能的封装

# def 函数名（参数列表）:
#     语句
    # return 表达式

# 函数参数必须传递
# 函数参数必须按顺序传递

def myFun1(str):
    print(str + "yu is a good man")

myFun1("调用1")

# df fdfd fdfd
print("df","fdfd","fdfd")

# 给俩数字 返回俩数字的和
def sumNum(num1,num2):
    return num1 + num2

i = sumNum(3,4)
print(i)

# 值传递和引用传递
def fun1(te):
    te = 30

t = 10
fun1(t)
print(t)

def fun2(li):
    li[0] = 900
list1 = [3,4,5]
fun2(list1)
print(list1)

# 常量存储在常量区 修改会更换常量地址
a = 10
b = 10
print(id(a))
print(id(b))

# 关键字参数
def fun3(p1="34",p2="56"):
    print(p1,p2)

fun3(p2= "fhdfjk", p1="tyui")

# 默认参数
fun3()

# 不定长参数--元祖

def fun4(p1,*arr):
    print(p1)
    for x in arr:
        print(x)
fun4("a","b","c")

def fun5(**d):
    print(d)
    print(type(d))
fun5(a = 1,b = 2) #  必须这样传递


