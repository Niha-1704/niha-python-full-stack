n = int(input())
l = []
for i in range(n):
    d = {}
    name = input()
    id = input()
    d["name"] = name
    d["id"] = id
    l.append(d)
print(l)
new = []
search = input()
for i in l:
    if search.lower() in i["name"].lower():
        new.append(i)
print(new)