def decode(encoded,first):
    a =[]
    a.append(first)
    x =first
    for i in encoded:
        x^=i
        a.append(x)
    return a

n = int(input("enter the size of the array"))
encoded =[]
for i in range(n):
    ele=int(input("enter the elements"))
    encoded.append(ele)
first =int(input("enter the first element of array"))
print(decode(encoded,first))
