

# 对象是对客观事物的抽象，类是对对象的抽象



class Person():

    def introduce_self(self):
        print('hello my name is xxx')


person = Person()
print(id(person))
# print(type(person))
person.introduce_self()
person2=Person()
print(id(person2))
