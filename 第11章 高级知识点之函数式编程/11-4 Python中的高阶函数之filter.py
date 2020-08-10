

# filter 过滤

# 用于过滤有杂质的数据

# help(filter)


def my_func(x):
    return x%2!=0

print(type(filter(my_func,[1,2,3,4,56,7,8])))
print(list(filter(my_func,[1,2,3,4,56,7,8])))
