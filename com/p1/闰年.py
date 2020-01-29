y = int(input("请输入年份: "))
if y % 100 == 0:
    if y % 400 == 0:
        print("闰年")
    else:
        print("不是闰年")
else:
    if y % 4 == 0:
        print("闰年")
    else:
        print("不是闰年")
