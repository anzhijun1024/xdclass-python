



# def my_func(numbers):
#
#     total= 0
#     for i in numbers:
#         total+=i
#     return total
def my_func(*numbers):
    print(type(numbers))
    total= 0
    for i in numbers:
        total+=i
    return total


# print(my_func([2, 5, 109]))
print(my_func(1,2,3,4,5))



