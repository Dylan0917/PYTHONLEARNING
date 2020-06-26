# -*- coding: UTF-8 -*-
# str = input()
endstr = "end"
str=""
for line in iter(input,endstr):
    str+=line+"\n"

print(str)