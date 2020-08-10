# help(map)


# map(func,[1234124])




def add(x):
    return x+1

result = map(add,[1,2,3,4])
result1 = map(lambda x:x+1,[1,2,3,4])
print(type(result))

print(result)
print(list(result))
print(list(result1))

#
# [1,2,3]
# [4,5,6]



result2= map(lambda x,y:x+y,[1,2,0,7],[4,5,6,4,5,6,78])
print(list(result2))

