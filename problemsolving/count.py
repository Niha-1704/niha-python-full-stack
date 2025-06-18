posts = [
    {"user":"alice","post":"hi"},
    {"user":"bob","post":"hello"},
    {"user":"alice","post":"again"},
    {"user":"x","post":"xyz"},
    {"user":"bob","post":"again"},
]

new = {}
for i in posts:
    if i["user"] in new:
        new[i["user"]] += 1
    else:
        new[i["user"]] = 1
print(new)
