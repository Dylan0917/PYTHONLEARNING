def fun1():
    print("this is fun1")
def outer1(f):
    print("**********")
    f()
outer1(fun1)

print("---------------------------------------------")

def outer2(f):
    def inner():
        print("**********")
        f()
    return inner;
@outer2
def fun2():
    print("this is fun2")

fun2()

# 通用装饰器

def outer3(f):
    def inner(*args, **kwargs):
        print("&&&&&")
        f(*args, **kwargs)
    return inner
print("---------------------------------------------")
@outer3
def f3(name,age):
    print("my name is %s, I am %d years old " % (name,age))

f3("yu",27)