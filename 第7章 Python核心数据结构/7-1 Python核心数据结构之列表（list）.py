




a = [1,2,3]
print(a)
print(type(a))

print(id(a))
print(id(a[0]))


a.append(4)
print(a)

del a[0]
print(a)

# a.pop(4)
print(a)
print(len(a))

print(a[0])
print(a.pop(2))
print(a)
print(a[-2])
print(a.index(3))
a.insert(1,4)
print(a)

print(a[0])
print(a)

print(a.pop(0))
print(a)

# 列表是有序的
# 列表里面的数据可以重复出现
b = [1,2,3,4,2,3]
print(b)
print(set(b))