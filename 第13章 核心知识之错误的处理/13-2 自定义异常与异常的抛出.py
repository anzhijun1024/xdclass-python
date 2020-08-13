'''
课程简介：介绍如何在python中自定义异常，以及手动抛出异常
虽然python中提供了非常多的内置异常类，但是，在平时开发中，针对特定的业务，可能需要自定义异
常，此时怎么办？
通过自定义继承Exception类的类，可以实现异常的自定义
'''

class MyException(Exception):
    def __init__(self,parameter):
        err = '非法入参{0}，分母不能为0'.format(parameter)
        Exception.__init__(self,err)
        self.parameter=parameter