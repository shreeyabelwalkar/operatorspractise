lst=['ssscgf','fgdtrddgf',23,45.-89,24]
print("lst is stored in memory having id",id(lst))

a=10
print("a is stored in memory having id",id(a))

a=10
b=20
if(a is b):
    print('a and b having same identity')
else:
    print('a and b not having same identity')

a=10
b=20
if(a is not b):
    print('a and b not having same identity')
else:
    print('a and b having same identity')

a = 10
b = 20
print(a is not b)
print('id of a=',id(a))
print('id of b=',id(b))


