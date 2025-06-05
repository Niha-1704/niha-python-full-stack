#find the element present in the list
l = [2,3,5,7,9,11,14]
n = int(input("Enter any number: "))
for i in range(len(l)):
    if l[i] == n:
        print("Found")
        break
else:
    print("Not Found")

for i in l:
    if n == i:
        print("Found")
else:
    print("Not Found")