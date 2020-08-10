#
#
# power = lambda x : x**2
#
# print(power(3))
#
#
# print((lambda x : x**2)(5))
#
# # 多个入参
# power = lambda x,n : x**n
#
# print(power(3, 2))
#
# # 函数过于复杂不要用lambda 用函数
#
# def add(l=[]):
#     return [x+1 for x in l]
#
#
# print(add([1, 2, 3]))



# 简介实现

def add(func, l=[]):
    return [func(x) for x in l]

print(add(lambda x:x+1, [1,2,3]))
print(add(lambda x:x+2, [4,2,3]))