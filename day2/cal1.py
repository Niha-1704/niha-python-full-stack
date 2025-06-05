n1 = int(input("Enter num1: "))
op = input("Enter op: ")
res = n1
while(op != "="):
    n2 = int(input("Enter num2: "))
    if op == "+":
        res += n2
    elif op == "-":
        res -= n2
    elif op == "*":
        res *= n2
    elif op == "/":
        res /= n2
    op = input("op: ")
print("result: ",res)     