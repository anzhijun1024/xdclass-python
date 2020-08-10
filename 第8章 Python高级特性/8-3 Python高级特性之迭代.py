
from  collections.abc import  Iterable


# 判断对象是否为可迭代对象  使用 isinstance()



a =[1,2,3,4]

print(isinstance(a, Iterable))    # True


# python 常见的可迭代对象  列表、元组、字符串、字典 无论有没有下表都是可以迭代的

d = {1:"111", 2:"222",3:'222'}

for i in d:
    print(d[i])
    print(i)

# 可迭代对象是成对出现的
j = [[1,2],[2,3]]

for x,y in j:
   print("x+y=", x+y)



