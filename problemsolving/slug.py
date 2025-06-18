def slug_generator(string):
    s = string.lower()
    s =list(s)
    res = ""
    for i in range(0,len(s)):
        if s[i].isalnum():
            res += s[i] 
        elif s[i] == " ":
            res += "-"
        else:
            continue
    return res
title = input()
result = slug_generator(title)
print(result)


# def slug_generator(string):
#     s = string.lower()
#     res=""
#     for i in s:
#         if not i.isalnum():
#             continue
#         elif i == " ":
#             res += "-"
#         else:
#             res += i
#     return res
# title = input()
# result = slug_generator(title)
# print(result)