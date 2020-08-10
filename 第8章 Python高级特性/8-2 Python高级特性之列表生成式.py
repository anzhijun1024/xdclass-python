

# print(list(range(0, 5)))


# for i in 可迭代对象（列表， 元组）

print([x * 2 for x in range(1, 11)])
print([x * 2 for x in range(1, 11)])
#

# 100以内所有偶数的列表
print([i for i in range(1, 101) if i % 2 == 0])
print([i for i in range(1, 101) if i % 2 == 1])


# 列表生成式支持双层循环

print([[x, y] for x in range(1, 3) for y in range(6)])


