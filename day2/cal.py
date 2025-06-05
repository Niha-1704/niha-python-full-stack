n1 = int(input("Enter num 1: "))
op = input("Enter operator: ")
res = n1
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
elif op == "%":
    print(n1 % n2)
elif op == "//":
    print(n1 // n2)
elif op == "**":
    print(n1 ** n2)
else:
    print("Enter correct operator")