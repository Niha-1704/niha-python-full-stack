file = open("./test.txt" , "w")
data = file.write("Ram sir is our trainer")
#print(data)
#file.close()

file = open("./test.txt" , "a")
data1 = file.writelines([
    "\nsir is teaching very well\n"
    "all the students are understanding the concepts\n"
])

file = open("./test.txt","r")
print(file.read())

file.close()