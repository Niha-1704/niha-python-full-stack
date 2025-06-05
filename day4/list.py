mylist = [10,20,"srinu",90.2]

mylist.append([3,"sailu",90])
print(mylist)

#mylist.pop()
#print(mylist)

mylist.pop(2)
print(mylist)

mylist.insert(3,"Niha")
print(mylist)

list1 = []
list1.append("janu")
print(list1)

list1.extend(mylist)
print(list1)

#pop an element inside nested list
list1[5].remove(90)
print(list1)