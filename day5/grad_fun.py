def add_stu(gradebook):
    name = input("Enter name : ")
    marks = list(map(int,input("Enter student marks : ").split(" ")))
    gradebook[name] = marks

def view_stu(gradebook):
    for n, m in gradebook.items(): 
        print(f"{n} : {m}  , avg :",sum(m)/len(m))
 
def  find_stu(gradebook):
    name_to_find = input("Enter the name : ")
    print(f"{name_to_find} : {gradebook[name_to_find]}")

def update_stu(gradebook):
    name = input("Enter name  to be updated : ")
    if name in gradebook:
        test_marks = list(map(int,input("Enter new marks : ").split(" ")))
        gradebook[name] = test_marks
        print(f"{name} : {test_marks}")
    else:
        print("Not Found")
    
def remove_stu(gradebook):
    name_to_remove = input("Enter the name : ")
    del gradebook[name_to_remove]