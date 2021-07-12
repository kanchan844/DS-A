def isPallin(s):
    new =""
    s = s.lower()
    for i in s:
        if i.isalnum():
            new = new+i
    return new == new[::-1]
s = input("enter the string")
print(isPallin(s))
