#creating a set
s = {11,"rani",12.0}
print(s)

#add element into set
s.add(10)
s.add("Devara")
print("After adding : ",s)

#typecast
l = ["niha" , "janu", "srinu"]
t = set(l)
print("after typecast: ",t)

#removing an element
s.remove(10)
print("After removing element: ",s)

#discard an element
s.discard(10)
print("After removig element:",s)

a = {1,3,4,55,5}
b = {88,4,55,5,2,9}
print(a)
print(b)

#union
print("union operation:",a.union(b))

#intersection
print("intersection operation: ",a.intersection(b))

#difference
print("difference: ",a.difference(b))

#symmetric_difference
print("Symmetric_difference: ",a.symmetric_difference(b))