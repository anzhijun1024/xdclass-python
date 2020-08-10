


t = (1,2,3)

print(type(t))

print(t)

r = (1)
print(type(r))
print(r)


# 元组必须加逗号

# 元组无法修改，新增，删除  可以取值和list语法一致
print(t[0])
print(t[-1])


# 作业题  把 111改为444
s = (1,2,3,['111','222','333'])
s[3][0]='444'
print(s)

s[3]='666'   # 不可遍历
print(s)
