# # 列表推导式
#
#
# a  = [x for x in range(0,10)]
# print(a)
# print(type(a))
# print(type(range(0,10)))
#
# b = (x for x in range(0,10))
# print(b)
# print(type(b))
# print(repr('0'))
# print(str('0'))


import os
class A:
    def __new__(cls, *args, **kwargs):
        print("this is __new__")
        return object.__new__(cls)
    def __init__(self):
        print("This is __init__")
    def res(self):
        print("This is res")
a =A().res()
b= A()
print("——————————————————————————————调试————————————————————————————-")
print(type(type))
print(type(int))
print(A)
print(type(A))
print(b)
print(type(b))
print(a)
print(type(a))
print(type(9))
print(type(object))
