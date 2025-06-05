#Count the number of vowels in a string
n = input("Enter a string: ")
v = ['a','e','i','o','u']
c = 0
for i in range(len(n)):
    if n[i] in v:
        c += 1
    i += 1
print("Number of vowels in string is: ",c)