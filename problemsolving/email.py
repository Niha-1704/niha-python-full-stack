def validate(s):
    if "@"  in s and "." in s:    
        return True
    else:
        return False
n = input()
s = n[1:-1]
print(validate(s))