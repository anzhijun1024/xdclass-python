



# 字典  {key：value}

a = {1:1,2:3}
print(a)
print(type(a))

a.update({3:3})
print(a)

del a[1]
print(a)

print(a[2])

a[2] = '2354'
print(a)

print(len(a))

for i in a:
    print(a[i])

a.update({3:"9879879"})
print(a)

# 字典中的key是不可变的
r= {[1,23,3]:3434}
print(r)