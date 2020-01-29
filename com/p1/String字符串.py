str1 = "a "
str2 = "b"
print(str1 + str2)

str3 = "good"
print(str3 * 3)  # goodgoodgood
# 访问字符
print(str3[0])  # g
# str3[0] = "d" 报错 字符串不可变

# 截取字符串 oo 算头不算尾
print(str3[1:3])

print("oo" in str3)  # True

# 格式化输出
num = 10
f = 10.1
print("num = %d,str3 = %s, f= %.2f" % (num, str3, f))
# 转义字符
print("\\n")
print('tom is a \'good\' man')
# 多个换行
print('''
a
b
c
d
''')
# r 表示内部的字符不转义
print(r"\n")
# eval() 函数用来执行一个字符串表达式，并返回表达式的值
print(eval("12-3"))
print(len(str3))  # 字符串长度
print(str3.lower())
print(str3.upper())
str4 = "SUNK is A GooD man"
print(str4.swapcase())
print(str4.capitalize())
print(str4.title())
print(str4.center(46, "-"))   # --------------SUNK is A GooD man--------------
print(str4.ljust(46, "-"))  # SUNK is A GooD man----------------------------
print(str4.zfill(42))  # 000000000000000000000000SUNK is A GooD man
print(str4.count("o"))  # 2
print(str4.count("o", 0, len(str4)))  # 2
print(str4.find("o"))  # 11 从左到右第一次出现的下标 没有返回-1
print(str4.rfind("o"))  # 12 从右第一次出现的下标 没有返回-1
print(str4.find("o", 12, len(str4)))  # 12 从左到右第一次出现的下标 没有返回-1

# print(str4.index("ss"))  # 如果不存在则会报错 其他和find一样
str5 = "          you are a good man    "
print(str5.lstrip())  # 去除左侧的空格
print(str5.rstrip())  # 去除右侧的空格

str6 = "**************you are a good man***********************"
print(str6.lstrip("*"))  # 去除左侧的*
print(str6.rstrip("*"))  # 去除右侧的*






