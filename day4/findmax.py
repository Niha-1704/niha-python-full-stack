l = [2,3,50,7,9,20,14]
m = l[0]
for i in range(1,len(l)):
    if m > l[i]:
        m = m    
    else:
        m = l[i]
print("Maximum element: ",m)