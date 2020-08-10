# def power(x, n=2):  # 默认参数在后面
#     return x ** n
#
#
# def power1(n=2, x):  # 默认参数在后面
#     return x ** n
#
#
# x
# print(power(2, 3))
# print(power1(4))
#
# # 给n设置一个默认值


def test(a=1,b=2,c=3):
    print('a=%d b=%d c=%d'%(a,b,c))
    return a,b,c

print(test(b=23))


def test1(l=[]):
    l.append('end')
    print(l)

test1([1,2,3])
test1([1,2,4])


test1()
test1()


# 编写默认参数时，默认参数必须指向不可变的对象 比如字符串，数字  元组