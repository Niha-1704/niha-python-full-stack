try:
    n1 = int(input("n1 : "))
    n2 = int(input("n2 : "))
    r = n1 / n2
    print(f"result is {r}")
except Exception as e:
    print(f"error occured as {e}")
else:
    print("No error occured")
finally:
    print("end of the program") 