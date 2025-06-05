import math
num = int(input("Enter : ")) 
s = 0
for i in range(1,int(math.sqrt(num))+ 1):
    if num % i == 0:
        s = s + i
if num == s:
    print("True")
else:
    print("False")