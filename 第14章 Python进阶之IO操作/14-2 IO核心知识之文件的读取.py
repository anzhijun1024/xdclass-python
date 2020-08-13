'''
在python里面，可以使用open函数来打开文件，具体语法如下：
open(filename, mode)
filename：文件名，一般包括该文件所在的路径
mode  模式
如果读取时读取中文文本，需要在打开文件的时候使用encoding指定字符编码为utf-8

'''

'''

'''

# try:
#     file = open(r'C:\Users\Administrator\Desktop\23132_金枸杞粉色枸杞20元扫码卡_50001.txt', 'r', encoding='utf-8')
#     print(file.readline())
#     # print(file.readlines())
#     # print(file.read()
# finally:
#     file.close()

with open(r'C:\Users\Administrator\Desktop\23132_金枸杞粉色枸杞20元扫码卡_50001.txt', 'r', encoding='utf-8') as file:
    print(file.readline())
    print(file.read())

file.close()






