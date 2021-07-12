def CheckPallindrome(str):
    new =''
    str = str.lower()
    for i in str:
        if i.isalnum():
            new = new+i
    return new == new[::-1]

str = input()
print(CheckPallindrome(str))
