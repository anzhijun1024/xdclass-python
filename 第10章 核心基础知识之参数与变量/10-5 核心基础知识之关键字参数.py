#
#
# def person(name, **kwargs):
#     kwargs.update({'pet_name':'343','sex':'woman'})
#     print(name,kwargs)
#
#
# info= {'pet': '111', 'sex': 'man'}
# person('wiggen', **info)
#
# print(info)



# 形参，默认， 可变， 命名关键字参数， 关键字参数
def person1(name, sex='男',*num, pet_name, **info):
    print(name, sex,num, pet_name,info)

person1('花花','男',2,3,4,5,6,pet_name='23452',pet='cat')