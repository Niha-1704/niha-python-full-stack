a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c)
print(b is c)
print(1 in a)
a[0] = 5
print(a)
print(b[0])
print(b)
print(1 not in c)