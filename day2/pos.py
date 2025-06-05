#Check whether a number is positive, negative or zero 
n = int(input("n: "))
if n >= 0:
    if n == 0:
        print("Zero")
    else:
        print("positive")
else:
    print("Negative")