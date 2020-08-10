


a = set()

# a.add(1)
print(a)

a.update([2,3,"1234124",'retgkjdfs'])
print('@@@@@@')
print(a.pop())
print(a)
print('@@@@@@')


# a.remove(2)
#
# print(a)

# a.remove(9)
print(a)


a.discard(0)
print(a)

print(len(a))

a.clear()
print(a)


s= {1,2,3}
s1 = {2,3,4}
union = s.union(s1)
print(union)


#集合无序
d = {'1','2','3'}

print(d)

f = {1,3,6,4}

print(f)

print(hash(1))
print(hash(2))
print(hash(6))
print(hash(4))

d = {'1','1','1'}
print(d)