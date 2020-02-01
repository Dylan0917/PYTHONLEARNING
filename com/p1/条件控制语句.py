# 从前往后匹配 匹配到则执行 匹配不到执行false
if False:
    print("100")
elif 1 == 1:
    print("101")
elif 2 == 2:
    print("102")
else:
    print("103")

# while-else语法
index = 1
while index <= 4:
    print("执行while")
    index += 1
else:
    print("执行else")

# else不在执行
# 如果当 while/for 循环中执行了跳出循环的语句，比如 break，将不执行 else 代码块的内容；
index = 1
while index <= 4:
    print("执行while")
    index += 1
    if index == 2:
        break
else:
    print("执行else")