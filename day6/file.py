file = open("./names.txt" , "r")
data1 = file.readline()
print(data1)
#file.close()

file = open("./names.txt" , "r")
data = file.read()
print(data)
#file.close()

file = open("./names.txt" , "r")
data3 = file.readlines()
print(data3)
#file.close()

file  = open("./names.txt","a")
data4 = file.append("we are learning python ")
