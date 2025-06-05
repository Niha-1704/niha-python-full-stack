file = open("./names.txt", "r")
data  = file.read()

list_data = data.split("\n")
print(list_data)

age_dict = {

}

for i in list_data:
    splitted_data = i.split(" ")
    print(splitted_data)
    age_dict[splitted_data[0]] = splitted_data[1]
print(age_dict)