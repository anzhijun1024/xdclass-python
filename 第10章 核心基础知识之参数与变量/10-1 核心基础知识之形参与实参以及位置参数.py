



# 形参   也叫形式参数  在函数定义的时候指定的可以接收到参数


def my_max(a,b):
    print(a)
    print(b)
    return a if a>b else b


# print(my_max(4, 7))   # 4,7 为实际参数
# 实参



# 位置参数
print(my_max(b=4, a=17))   # 4,7 为实际参数


