#creating
dict = {"age" : 10}
print("dictonary: ",dict)

#adding
dict["name"] = "niha"
print("After Adding:",dict)

#iteration
for i in dict:
    print(f"{i} : {dict[i]}")

#accessing
print("accessing:",dict["age"])

#modify
dict["age"] = 20
print("After modifying: ",dict)

#delete
del dict["age"]
print("After deleting: ",dict)

#accessing key - value pairs
print(dict.items())

#accessing keys
print(dict.keys())

#accessing values
print(dict.values())