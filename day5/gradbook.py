import grad_fun as gf

gradebook = {}

while True:
    print("student Grade Book")
    print(" 1. Add Student ")
    print(" 2. view the student details")
    print(" 3. find the student details")
    print(" 4. update the marks ")
    print(" 5. remove the student")
    print(" 6. Exit")
    n = int(input("Enter choice: "))
    if n == 1:
        gf.add_stu(gradebook)
    elif n == 2:
        gf.view_stu(gradebook)
    elif n == 3:
        gf.find_stu(gradebook)
    elif n == 4:
        gf.update_stu(gradebook)
    elif n == 5:
        gf.remove_stu(gradebook)
    else:
        break
