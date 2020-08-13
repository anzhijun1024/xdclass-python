from chapter12.my_exception import MyException

def my_fun(x):
    if x==0:
        raise MyException(x)
    return 12/x


# print(my_fun(0))


def my_func():
    try:
        print(10/0)
    except ZeroDivisionError:
        print('除数不能为0')
        raise

my_func()