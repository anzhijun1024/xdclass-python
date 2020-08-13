'''
课程简介：介绍什么是单元测试，以及如何编写单元测试
什么是单元测试
单元测试（英语：Unit Testing）又称为模块测试，是针对程序模块（软件设计的最小单位）来进
行正确性检验的测试工作。程序单元是应用的最小可测试部件。在过程化编程中，一个单元就是
单个程序、函数、过程等；对于面向对象编程，最小单元就是方法，包括基类（超类）、抽象
类、或者派生类（子类）中的方法。
简而言之：就是写一段代码，用来验证另一段代码在特定情况下的正确性
单元测试的好处与“坏处”
好处：减少bug、提高代码质量、可以放心重构（在未来修改实现的时候，可以保证代码的行为
仍旧是正确的）
"坏处"：占用开发时间，尤其是在起步阶段


'''


class MyTest():
    def my_add(self, a, b):
        # def my_add(a, b):
        return a + b
