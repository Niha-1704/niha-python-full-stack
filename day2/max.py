#Find the largest among three numbers
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a > b and a > c:
    print(f"{a} is big")
elif b > c:
    print(f"{b} is big")
else:
    print(f"{c} is big")    