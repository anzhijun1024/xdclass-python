'''

在平时的开发中，一般会有多模块，为了软件的复用性，我们通常在模块之间相互引用，已达到复用的
目的。
a = 1
b = 2
print(globals())
输出结果：
{
  '__name__': '__main__',
  '__doc__': None,
  '__package__': None,
  '__loader__': <_frozen_importlib_external.SourceFileLoader object at
0x00000255B062F548>,
  '__spec__': None,
  '__annotations__': {},
  '__builtins__': <module 'builtins' (built-in)>,
  '__file__': 'C:/Users/wiggin/Desktop/xdclass/chapter12/class2.py',
  '__cached__': None,
  'a': 1, 'b': 2
}
def my_func():
  x = 123
  print(locals())
  locals()["x"] = 456
  print("x=", x)
y = 123
my_func()
globals()["y"] = 111
print("y=", y)
在python中，可以使用import 关键字进行模块的导入，语法如下：
import module_name
例如，在模块class2中要引用同目录下class1中的变量a，此时可以如下

'''

import  importlib
importlib.import_module()