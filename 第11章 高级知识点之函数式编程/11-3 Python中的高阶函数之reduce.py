# reduce 函数

# from functools import reduce
from functools import reduce


# reduce(function,sequence=,initial=)
# reduce(function,[1,2,3])

# function(function(1,2),3)


# 使用reduce 进行乘积

def func(x, y):
    print(x, y)
    return x * y


print(reduce(func, [1, 2, 3, 4, 5, 6],3))
print(reduce(lambda x,y:x*y, [1, 2, 3, 4, 5, 6]))
