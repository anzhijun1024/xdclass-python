



class Person():
    def __init__(self,name,age,height):
        print('hello world')
        self.name = name
        self.age =age
        self.height = height
    def add_num(self,a,b):
        return a+b

    def introduce_self(self):
        print('名字： %s, 年龄：%s,身高:%s'%(self.name,self.age,self.height))

person= Person('花花',23,185)

print(person.add_num(2,3))
person.introduce_self()