#Write a program to find the factorial of a number
n = int(input("n: "))
res = 1
for i in range(1,n+1):
    res = res * i
print(res)