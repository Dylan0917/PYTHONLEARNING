import functools


print(int("1010",base=2))
print("---------------------------------------------")

def int2(inpa):
    return int(inpa,base=2)
print(int2("1010"))
print("---------------------------------------------")


int3 = functools.partial(int,base=2)
print(int3("1011"))