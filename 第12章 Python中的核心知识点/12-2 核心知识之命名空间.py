"""
课程简介：介绍python中核心的知识点----命名空间
什么是命名空间
命名空间是变量到对象的映射集合。一般都是通过字典来实现的。主要可以分为三类：
1、每个函数都有着自已的命名空间，叫做局部命名空间，它记录了函数的变量，包括函数的参
数和局部定义的变量。
2、每个模块拥有它自已的命名空间，叫做全局命名空间，它记录了模块的变量，包括函数、
类、其它导入的模块、模块级的变量和常量。
3、还有就是内置命名空间，任何模块均可访问它，它存放着内置的函数和异常。
通俗点讲：命名空间就是为了确定全局唯一，当模块A中有变量c，模块B中也有一个变量c，此
时，通过A.c来确定引用A中变量c.123
比如在class2模块中要引用class1中的变量a，在导入class1模块之后，可以使用class1.a访问class1中
的变量
命名空间的查找顺序
当一行代码要使用变量 x 的值时，Python 会到所有可用的名字空间去查找变量，按照如下顺序：
1、局部命名空间：特指当前函数或类的方法。如果函数定义了一个局部变量 x，或一个参数
x，Python 将使用它，然后停止搜索。
2、全局命名空间：特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python
将使用它然后停止搜索。
3、内置命名空间：对每个模块都是全局的。作为最后的尝试，Python 将假设 x 是内置函数或
变量。
4、如果 Python 在这些名字空间找不到 x，它将放弃查找并引发一个 NameError 异常，如，
NameError: name 'xxx' is not defined。
当函数嵌套时的查找规则
1、先在当前 (嵌套的或 lambda) 函数的命名空间中搜索
2、然后是在父函数的命名空间中搜索
3、接着是模块命名空间中搜索
4、最后在内置命名空间中搜索

"""

msg = 'msg'
def my_func():
    name = 'wiggen'
    def func_son():
        name= 'xdclass'
        print('内部方法的名字：',name)

    # 调用内部函数
    func_son()
    print(name)

my_func()




a= 1
def my_func(str):
    global a
    if a ==1:
        print(str)
        a=24

my_func('file')
print(a)

'''

命名空间的访问
局部命名空间的访问
局部命名空间可以 locals() 来访问。
'''
def my_func1():
    a=52
    b=2
    print(locals())


print(type(my_func1()))
d= my_func1()
print(d)


a=1
b=3
print(globals())


'''
locals 与 globals 之间的区别
locals 是只读的，但globals是可读写的

'''


def my_func():
    x=123
    print(locals())
    locals()['x']=222
    print(locals())
    print('x=',x)
y=234
my_func()
globals()['y']=111
print('y=',y)