def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file = open("./contactapp.txt","a")
    file.write(f"{name} : {mobile}\n")
    file.close()

def view_contacts(contacts):
    print("\n")
    file = open("./contactapp.txt","r")
    data = file.readlines()
    if not file:
        print("Not found")
    for i in data:
        print(i)
    file.close()
     

def delete_contact(contacts):
    file=open("./contactapp.txt","r")
    data =file.readlines()
    file.close()
    name_to_delete = input("Enter contact name to delete :")
    delete = False
    file = open("./contactapp.txt", "w")
    for key in data:
        name = key.split()
        print(name)
        if name_to_delete == name[0]:
            delete = True
            continue
        else:
            file.write(key)
    if not delete:
        print(f"The {name_to_delete} contact not found")
    else:
         print(f"The contact {name_to_delete} is deleted")
    file.close()
     

def find_contact(contacts):
    query = input("Enter name to search : ")
    file = open("./contactapp.txt","r")
    data = file.readlines()
    flag = False
    for key in data:
        if query in key:
            print(key)
            flag = True
    if not flag:
        print("Not found")
    file.close()


def edit_contact(contacts):
    file = open("./contactapp.txt", "r")
    data = file.readlines()
    file.close()
    name_to_edit = input("Enter contact name to edit: ").lower()
    number = int(input("Enter the number: "))
    file = open("./contactapp.txt", "w") 
    for key in data:
        name=key.strip("\n").split("=")
        #print(name)
        if name_to_edit == name[0]:
            file.write(f"{name_to_edit}={number}\n")
        else:
            file.write(key)
    file.close()