'''
什么是错误
简而言之：还没运行，在语法解析的时候，就发现语法存在问题，这个时候就是错误，比
如，
'''


'''
print('hell word'
# SyntaxError: unexpected EOF while parsing
'''

'''
什么是异常
简而言之：代码写好之后，无明显语法错误（这个时候，编辑器不知道有错，语法解析时也
不知道有错），但是运行的时候，会发生错误，这个时候称之为异常，比如
'''

# print(10/0) # ZeroDivisionError: division by zero


# 什么是警告

import warnings
def fxn():
    warnings.warn('deprecated', DeprecationWarning)


'''
异常的处理形式如下：
    try:
    你要做的可能会发生异常的事
    except 可能会发生的异常:
    发生异常之后要做的事
    except 可能会发生的异常2:
    发生异常之后要做的事2
    finally：
    最终要做的事情

'''

# 例如
try:
    print(10/1)
except ZeroDivisionError:
    print('除数不能为0')
try:
    with open(r'C:\Users\Administrator\Desktop\23132_金枸杞粉色枸杞20元扫码卡_5000.txt') as f:
        for line in f:
            print(line,end='')
except FileNotFoundError:
    print('文件不存在')

