# list1 = [1,2,3,4,5,0,3,0,4,0,5,6]
# l1 = []
# l2 = []
# for i in list1:
#     if i == 0:
#         l2.append(i)
#     else:
#         l1.append(i)
# l1.extend(l2)
# print(l1)

# list = [1,2,3,4,5,0,3,0,4,0,5,6]
# index = 0
# for i in range(len(list)):
#     if list[i] != 0:
#         list[index] = list[i]
#         index += 1
# for i in range(index, len(list)):
#     list[i] = 0
# print(list) 

a = [ 1,2,3,4,6]
b = [5,6,7,8]
c = a + b
for i in range(len(c)):
    if c[i]