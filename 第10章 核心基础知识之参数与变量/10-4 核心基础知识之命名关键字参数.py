


def person(name, *,sex):
    print(name,sex)

person('哈哈', sex='男')



def person1(name, sex,*args):
    print(name,sex,args)

person1('哈哈', '男','23')