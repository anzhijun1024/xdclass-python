


# 列表生成器一边生成一边计算


print(type([x*2 for x in range(5)]))
print(type((y*2 for y in range(5))))

generator=(y*2 for y in range(5))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for i in generator:
    print(i)