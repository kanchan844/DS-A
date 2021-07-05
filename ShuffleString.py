def shuffle(indices,s):
    s1=[0]*len(s)
    for i in range(len(s)):
        s1[indices[i]] = s[i]
    s1 = ''.join(s1)
    return s1
s=input("enter the string")
indices=[]
n = int(input("enter the length of the indices array"))
for i in range(n):
    ele=int(input("enter the elements"))
    indices.append(ele)

print(shuffle(indices,s))
